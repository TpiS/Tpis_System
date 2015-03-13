#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ====================
# ライブラリの呼び出し
# ====================
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from sklearn import datasets
from sklearn.cross_validation import StratifiedKFold
from sklearn.externals.six.moves import xrange
from sklearn.mixture import GMM

def make_ellipses(gmm, ax):
    """
    GMM の学習結果を楕円でプロット（一枚分）

    引数:

        - gmm : gmm でクラスタリングをした結果
        - ax : subplot の数
    """
    for n, color in enumerate('rgb'):
        v, w = np.linalg.eigh(gmm._get_covars()[n][:2, :2])
        u = w[0] / np.linalg.norm(w[0])
        angle = np.arctan2(u[1], u[0])
        angle = 180 * angle / np.pi  # convert to degrees
        v *= 9
        ell = mpl.patches.Ellipse(gmm.means_[n, :2], v[0], v[1],
                                  180 + angle, color=color)
        ell.set_clip_box(ax.bbox)
        ell.set_alpha(0.5)
        ax.add_artist(ell)

iris = datasets.load_iris()  # サンプルデータ

# Break up the dataset into non-overlapping training (75%) and testing
# (25%) sets.
skf = StratifiedKFold(iris.target, n_folds=4)  # 交差検定を行うためデータを４分割
train_index, test_index = next(iter(skf))      # 訓練データとテストデータのインデックスを取得

# 取得したデータ番号からサンプルデータを呼び出し
## 訓練データ
X_train = iris.data[train_index]
y_train = iris.target[train_index]
## テストデータ
X_test = iris.data[test_index]
y_test = iris.target[test_index]

# クラスタ数を定義
n_classes = len(np.unique(y_train))

# 異なる共分散のタイプでGMMを試す
classifiers = dict((covar_type, GMM(n_components=n_classes,
                    covariance_type=covar_type, init_params='wc', n_iter=20))
                   for covar_type in ['spherical', 'diag', 'tied', 'full'])

# 学習結果の大きさを取得
n_classifiers = len(classifiers)

# 可視化設定
plt.figure(figsize=(3 * n_classifiers / 2, 6))
plt.subplots_adjust(bottom=.01, top=0.95, hspace=.15, wspace=.05,
                    left=.01, right=.99)


for index, (name, classifier) in enumerate(classifiers.items()):
    # 訓練データに対する class labels があるので,
    # GMM parameters を教師データとして初期化することが可能
    classifier.means_ = np.array([X_train[y_train == i].mean(axis=0)  # それぞれのクラスタ別に
                                  for i in xrange(n_classes)])        # 平均値を取得

    # EM algorithm を使って他の GMM parameters を推定
    classifier.fit(X_train)

    # 学習結果の可視化
    h = plt.subplot(2, n_classifiers / 2, index + 1)
    make_ellipses(classifier, h)

    # 元データを散布図でプロット
    for n, color in enumerate('rgb'):
        data = iris.data[iris.target == n]
        plt.scatter(data[:, 0], data[:, 1], 0.8, color=color,
                    label=iris.target_names[n])

    # テストデータを X でプロット
    for n, color in enumerate('rgb'):
        data = X_test[y_test == n]
        plt.plot(data[:, 0], data[:, 1], 'x', color=color)

    # クローズドテスト
    y_train_pred = classifier.predict(X_train)
    train_accuracy = np.mean(y_train_pred.ravel() == y_train.ravel()) * 100
    # 評価値を plot に反映
    plt.text(0.05, 0.9, 'Train accuracy: %.1f' % train_accuracy,
             transform=h.transAxes)

    # オープンテスト
    y_test_pred = classifier.predict(X_test)
    test_accuracy = np.mean(y_test_pred.ravel() == y_test.ravel()) * 100
    # 評価値を plot に反映
    plt.text(0.05, 0.8, 'Test accuracy: %.1f' % test_accuracy,
             transform=h.transAxes)

    plt.xticks(())
    plt.yticks(())
    plt.title(name)

# 各プロットのタイトルを追加
plt.legend(loc='lower right', prop=dict(size=12))
plt.show()
