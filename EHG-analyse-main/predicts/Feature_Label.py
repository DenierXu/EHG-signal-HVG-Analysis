def New_feature(path, Original_Feature):
    with open(path, 'r') as file_to_read:
        feature_All = []
        lines = file_to_read.readlines()
        for feature in Original_Feature:
            for line in lines:
                data = line.strip().split()
                sample_single = []
                if str(data[0]) == str(feature[0]):
                    sample_single.append(line.strip().split()[0].strip())
                    for i in range(1, len(data)):
                        sample_single.append(float(line.strip().split()[i].strip()))
                    for h in feature[1:]:
                        sample_single.append(h)
                if sample_single:
                    feature_All.append(sample_single)
        return feature_All


# "D:\Kinpeng_Zhang\Data_Select\First_Channel_8_New.txt"
def save_file(path, list):
    f = open(path, 'w+')
    for i in list:
        for j in i:
            f.write(str(j) + "     ")
        f.write("\n")
    f.close()


def do_Filter(Filter_Name, Channel_Number):
    Original_Feature = []
    with open(Filter_Name, 'r') as f:
        for line in f.readlines()[2:]:
            line_Feature = []
            if int(line.split("|")[1].strip()) is Channel_Number:
                line_Feature.append(line.split("|")[0].strip())
                # 1表示的是早产，0代表的是非早产
                if line.split("|")[9].strip() == "f":
                    line_Feature.append(0)
                else:
                    line_Feature.append(1)
                Original_Feature.append(line_Feature)
        return Original_Feature

Original_Feature = do_Filter("D:\\Kinpeng_Zhang\\Filter\\tpehgdb_features__filter_0.3_Hz-3.0_Hz.fvl", 3)
#  斜率特征
# feature_All=New_feature("E:\\Time_Fre_Domain\\Feature\\Third_Channel_Fre_Slop.txt",Original_Feature)
#  样本熵特征
feature_All = New_feature("E:\\Fre_domian\\Third_Channel_Fre_Slop.txt", Original_Feature)

# 斜率特征加早产或者非早产标记
# save_file("E:\\Time_Fre_Domain\\Feature_Merge\\Third_Channel_Fre_Slop_Merge.txt",feature_All)
# 样本熵特征加早产或者非早产标记
save_file("E:\\Fre_domian\\Third_Channel_Fre_Slop_label.txt", feature_All)
