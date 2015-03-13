#!/usr/bin/env python
# -*- coding: utf-8 -*-


##インポート##                                                                                                                        
import subprocess
import numpy
import struct
import sys
import codecs
import pickle
from sklearn import datasets
import csv
import os
import math

print["label","max","min","range","average","var","size"]



def feature(file,label):

##f０抽出##

    output = subprocess.check_output(['get_f0s',file])


##改行区切り##
    output = output.splitlines()


##無音区間削除##
    while '0.0' in output: 
        output.remove('0.000000')


##空要素削除##
    output = filter(lambda x:x!='',output)


##float変換##
    output = map(float,output)


##各指標計算##
    a = numpy.array(output)
    b = numpy.average(a)
    c = numpy.var(a)
    d = a.size
    e = max(output)-min(output)

   
    return [label,max(output),min(output),e,b,c,d]



high_files = [
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128162010_5739c2d8-61a0-48fe-affb-a9a032520644",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161947_e4ea735a-23bc-4e8f-800b-629e4b289522",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161941_03558c0e-5599-4a8c-8c5a-28582edb0101",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161919_d12f3b11-10a6-494b-b4e7-48cf0f531ff8",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161914_8264050a-1850-438e-90b0-b64e265fe3b2",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161908_49ba8750-819b-446f-8be0-b895d1cf4015",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161902_c2016174-5a1a-4205-8a9a-37cf656ff9ca",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161856_7305ebaf-8894-4f9e-b3ef-89e1620ad2ab",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161837_26114f7e-55df-4606-86bd-dade9fc752c2",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161825_2dde5929-8289-49df-a161-f5e0df06cd6b",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161820_6eb7f64f-9bee-4e6b-b796-1c37688bfb5d",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161816_d629d072-9c1c-4ac9-8cd7-d151ac3e8086",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161805_888f24dd-0938-46ad-bd1c-9c2b6e34bf8a",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161756_1a557f36-decb-4947-a2f2-0ac1189d229d",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161746_9c4cded2-9cfa-4366-a8d9-d9531ebad58c",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161740_11a7e508-03cd-4902-a38a-0ad1ff48a336",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161734_74886a30-d650-4cd3-a376-8f9d0661134f",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161729_781c7754-05b6-4da2-94cc-e1770f4e4317",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161724_e0f52f98-225c-423b-a31d-480343535666",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161712_31fbaf9f-48a8-426c-8316-90c702ac9496",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161704_bc53c4e9-4a69-4a66-aba4-bd84eb430e2f",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161652_54fd7069-eb4b-461b-8d06-1593dc64d819",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161608_6a38407c-9778-4df6-9291-2b4df011a406",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161604_3e4dd21c-8c06-401c-9bfe-eb80787d873d",
"/home/sugaya/Tpis_System/tadaima_high/suzuki_high_20150128161601_55e1c0b7-61c1-4bd8-924d-c03e5cb7bd28",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162757_4c2d654e-5c11-441b-b359-c69bc2a7ddc9",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162742_58c89452-e311-4cd3-b794-1a38b73b7c76",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162735_d5987b1f-a8b4-44ec-afe1-7bde302819a8",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162730_78092c62-0021-43f6-bfa7-53fc4a145492",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162724_8090d054-cef1-4b86-859f-de6f80af02ee",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162713_ff70abc8-888b-4926-b9b6-c0d75349f994",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162707_5a6bc847-268c-4344-811a-3feaf973bb6c",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162658_2bd07190-d93d-4072-90e6-6eae094c4c14",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162647_ec3c3f2e-b9ae-48d8-add7-d77c528fe3b2",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162643_4e6886c7-5d13-4a51-bc02-d34b19a891bd",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162636_9ae0cb5a-f473-494c-90ba-da130d6f9a22",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162620_deb27fe1-569e-472f-8d79-83595242417a",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162614_e8d98eb2-f68d-40d1-a895-fe13a38caf5e",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162607_4e05b526-cb3c-4ad3-abf9-bd0f916097eb",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162603_f348abd4-f5f2-46bb-992a-3e7256720f06",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162556_c5d8dc87-00ed-4f20-b251-9d71f89a7f06",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162549_218f626f-b618-453c-b1ac-0bccd6d219b3",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162541_f459a283-8dd3-450b-8ce4-272d83dd7b89",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162531_387a4e2f-c006-4efa-8d19-b90f7c1cef42",
"/home/sugaya/Tpis_System/tadaima_high/sugaya_high_20150128162519_b6c77913-cd59-43cc-bbec-6d3610c959c1",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163403_b275e600-5719-410c-8915-1b0bfefb5c8c",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163337_b01adb53-e26a-4057-b7d9-4a0045db9ec3",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163327_c338aa5c-e516-4fcc-bc2e-1def6b507354",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163323_d3847ac2-cb83-433e-a05f-3cef61fd0ffd",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163258_d1a24194-a262-4cc9-a6f7-73e67c2df67a",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163248_88809f3e-8b04-4243-8962-8974a43b1bb2",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163237_3ab5243e-5550-4bcc-b8aa-51b9cec3d7ad",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163230_32ce9ff5-21db-43c2-a5a2-d94ec86b067c",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163225_14798922-e531-41fc-9ade-f55cf1d6ebd5",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163214_27d89aac-1d54-4823-ad84-d761a5472edf",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163206_9ff87b17-3f42-48fa-ae31-19365aaa3bd6",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163153_76a82d90-478b-4102-8ffe-1f5bfdab6789",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163125_43cb7ad3-9465-41b3-aa58-aaf89b092400",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163116_8e1371f0-db89-4c6c-b45d-ca62cb4bb636",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163107_0066e53e-caed-4712-868b-76dbf73b9faa",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163057_e2de1552-b99a-4b12-938b-ea415ead2262",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163047_12cf370d-309b-4eb6-8050-b50dcb52e028",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163037_46b1db22-a608-4775-baf4-34f95fa122fc",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163030_73ddbd29-9b6d-44c9-8788-36233a8e9b7c",
"/home/sugaya/Tpis_System/tadaima_high/ogawa_high_20150128163013_0df105da-37a7-40c9-9f1a-eacb9f56b4b3",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162354_f91a7776-cb2b-4eea-bcec-fe79d386295b",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162346_ed7ef789-adcb-4713-8ff9-2e3cbe80fce0",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162341_78f96c19-ab39-4c92-8abd-3020fde22ca4",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162333_89c88a7a-e57e-44b6-92ce-115990526a2e",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162325_56aa8110-b613-4dc9-aae2-f3470cdc95f6",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162317_41a107b9-7ed7-4fa2-8736-714049696b52",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162309_326c613b-57e0-4c54-a154-f74c981f7f08",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162301_efe1d30f-06c6-4c48-91f8-59970ed790f0",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162252_43027249-9e78-46fe-9709-c28090960000",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162245_fcd976bf-c576-4c9d-8154-7b7285b32784",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162222_91ea9c9d-d504-4f4a-88af-067f27f8562d",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162213_e9662afd-75ef-4c45-af4f-b11699ab2d4a",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162151_25c18971-30d1-422b-a9c7-826b9e86efc3",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162143_d926ebda-d067-427a-bff0-3b8d04ac99ac",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162135_3b0bd7a1-0a71-441d-85ac-517edd51560f",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162128_03af8a9d-bf47-4668-85b9-0e16fcde5e01",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162122_b86228ad-f791-49fb-9da8-201c9fe4fddb",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162114_675923ce-5f8b-4248-8f92-c9333053e2b9",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162107_2ff00cd7-3623-4e05-9f22-23b3b50fbe85",
"/home/sugaya/Tpis_System/tadaima_high/ito_high_20150128162049_aae28645-6cf0-4de8-adb5-a75f9bd7e001"]

law_files = [
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163929_8aff7626-715d-478b-8246-999f49281ce1",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163910_73ab57a6-cb19-4c62-b5b0-63427dce57a1",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163901_47af5618-8226-4059-9c17-334118319daa",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163853_b4ace5d3-24f2-4aaf-822b-de89d1661b7f",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163844_54c3d8f4-2625-49d5-9b16-bdab16b9a54e",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163839_ae720af8-5ad9-46df-9fd8-7d718f8fc7b4",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163833_e3a130e6-0ea0-4426-8a60-fa7f2a677ad2",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163813_af8df2d9-ff1a-43b7-bc1c-005f8ab45e18",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163806_f2f8b8b1-1b55-4f07-9bae-c135a0a6598f",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163757_ab72766b-9e7f-4021-b24a-284f083990e7",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163752_c867214e-0414-4886-8dd0-17e16c08bc5d",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163746_d1df7004-f2f1-48d6-b725-c98146e173e3",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163736_89284e99-546c-4838-a967-1be9e814a285",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163727_6274cf5f-9b13-4696-8265-91427900a489",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163722_3a799975-2899-47ad-8ab2-1be06a5f0ec4",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163712_25bb21ed-1408-441b-9a03-47745dab4265",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163700_f8588b9b-9f2b-4003-b1f3-6aba41600c3d",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163649_1bbd58c2-c098-4d2f-9a12-5e95faca2942",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163645_6c958162-9dba-436e-b58a-3b618be544ae",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163637_6276aea6-5e0a-4c48-8701-bded949a4e5a",
"/home/sugaya/Tpis_System/tadaima_law/suzuki_low_20150128163531_f6011c3a-73a4-4ba8-a8de-cb9d9e739c88",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164737_f85bb818-9ced-43c1-a82c-733191edd47e",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164731_e2998c97-28a6-4685-b01f-a0e2a26a72da",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164717_841d6cd1-c058-4431-8f54-023678507d44",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164701_e620fc3f-9065-4825-9197-a07cede1bca4",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164651_8af488f7-0d8b-4cf6-aa7d-96e169d37555",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164643_07d0aeb2-7810-4523-bf06-2b69697dc21c",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164631_affb8e2e-dfbd-4999-abcf-ec81da47e0d8",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164623_9e799c70-c187-487e-900a-9d6087e23196",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164615_9b3045ae-3cd5-421f-bb66-c6eef4e42914",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164605_b6b77294-9ec2-450e-9c2a-ea6adffa7c9a",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164555_64c2f132-7b0f-4040-9dbf-2bf23f95c492",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164550_8407aa0c-f750-4c11-a4de-e27867e31083",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164540_c334bfef-6fc0-4e1b-98b8-37dd3e711358",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164533_047ab794-b100-4a23-8423-b231ca12c117",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164521_d80b8c55-545d-4b1a-84f3-5973491f5595",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164514_adc3e470-6008-4da1-b1f1-f4e645f4554e",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164509_b559160d-1749-4234-bda2-377a82a0655f",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164502_9844b515-2409-452c-92f3-d0c97494b813",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164456_0baa90fb-573a-422b-b17e-a3a5245215a3",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164448_be3afa1d-4d0c-4e61-b377-3fcc4f50eef6",
"/home/sugaya/Tpis_System/tadaima_law/sugaya_low_20150128164432_13848915-3248-44b4-9535-133fae55743d",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165201_0b346213-9996-44a8-939c-0ecd159ebf9c",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165132_946956b5-de13-4331-abf5-b59245d5efa0",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165127_7066e0a4-52f8-482c-8941-48e30bd22130",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165123_fff321ce-8294-450c-8330-03257219ff6a",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165103_10ad885f-874e-4199-8f50-b213dd32db46",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165031_483bbdc6-f56f-420c-b5a8-cb6c91404098",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165026_79f6f4a7-9b36-4d65-bc98-72c7bda105be",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165021_d3fd7ebe-c286-4d71-8b03-88a065113564",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165016_f90518f5-50b8-46a5-b3c8-cd84db122075",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165011_7a09f8c1-22c9-480a-96f1-d3e51d656f3c",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128165001_bf22b800-d56f-462e-8191-1cb097f97066",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164945_e48e4aeb-fb56-4463-bc6d-0a39de3d23da",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164939_d584893a-92d3-4031-ac83-ff32053c5887",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164930_aa7279b9-62b5-4da9-a4a9-b7ae4260d87e",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164922_540850a6-4362-4375-9fef-97cf41c6bd0e",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164916_c00860ca-9438-4944-b21f-d259b505f6cf",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164906_29164983-c8bc-4f42-9810-cafaefc6f320",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164856_ad5f6bcb-38e2-46fe-8002-cbea3a128617",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164847_a4ccb993-8315-423c-b63c-12c74e5658b5",
"/home/sugaya/Tpis_System/tadaima_law/ogawa_low_20150128164831_9c598f76-ecbb-4724-8750-51db323efee6",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164321_b443ebe3-90d0-46e0-b161-c9b02b5e5501",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164315_1be330cf-47fa-4650-8999-db4c58fb333f",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164309_6a3cc2ae-2d4a-46f6-9c0d-ec1fff92889d",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164302_71b11bba-d677-450b-817c-c86e11ab65d4",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164255_8f105ef6-3a8c-4530-8f0c-7572fff0b511",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164248_4fefb622-8492-4bc2-9d93-28b403998920",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164242_0651c16e-e37b-4c57-8f96-fccad614ec55",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164232_eaab1772-ec07-40da-a7db-b0535aa4adc4",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164226_f8f96a66-65c4-4367-a35b-febbacaacf15",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164218_b3f717f4-11bf-4b60-a7ee-b69c6e0a8038",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164212_4e6a32b4-ba80-4224-980b-24b89dc73918",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164206_bbd1192d-c523-4eed-b468-35e9d5608edb",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164200_7019fe8a-97cb-4a5e-9afe-a4b56fa599db",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164154_f084df7e-f48b-484b-ad7c-fa722c922863",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164147_bd918529-2758-444b-a85b-72863bc27b7c",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164141_88273ff8-3321-4872-8fde-ec25fd2130b1",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164133_5c2bfdbe-a547-4473-a8e8-49b0b3904d3f",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164127_27e12610-2522-4631-a11d-3042962363c3",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164121_2d84d82b-a2be-49f9-9262-db88da0ef4ac",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164115_ee6cf8fe-d3d1-4ab1-a24e-8387dd6e2f9a",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164109_f3357c4d-512d-4532-8335-a86f0735b775",
"/home/sugaya/Tpis_System/tadaima_law/ito_low_20150128164058_de1a1940-054d-471d-98bc-6cece888ff57"]
 
feature_table = []




for file in high_files:
    print feature(file,'high')
    

for file in law_files:
    print feature(file,'law')


FILE ='f0_tadaima.csv'

f = open(FILE,'wb')

writecsv = csv.writer(f,lineterminator='\n')
writecsv.writerow(["label","max","min","range","average","var","size"])

for file in high_files:
    writecsv.writerow(feature(file,'high'))


for file in law_files:
    writecsv.writerow(feature(file,'law'))


f.close()
