import requests
#import combine_two_excel
import pandas as pd

# path_citation_imp = "citation imp.xlsx"
all_data = "all_data.xlsx"
# sheet = pd.read_excel(path_citation_imp, sheet_name="Sheet1")
data = pd.read_excel(all_data, sheet_name="Sheet1")#我们只用再把这个数据库的doi补全即可。
title = data.loc[:, 'Title']
title_list = []
for t in range(len(title)):
    # print(title[t])
    title_list.append(title[t])

def get_doi(title):
    # 构建 CrossRef API 的请求 URL
    base_url = "https://api.crossref.org/works"
    params = {"query.bibliographic": title}

    # 发送 GET 请求
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # 解析 JSON 响应并获取 DOI
        data = response.json()
        if data["message"]["items"]:
            doi = data["message"]["items"][0]["DOI"]
            return doi
        else:
            print("DOI not found")
            return None
    else:
        return "Request failed"

# 获取每篇论文的DOI
doi_list_for_citation_title_list = []
for title in title_list:
    doi = get_doi(title)
    doi_list_for_citation_title_list.append(doi)
    print(f"Title: {title}\nDOI: {doi}\n")
    print("length of doi_list is {} and length of citation_list is {}".format(len(doi_list_for_citation_title_list), len(title_list)))
print("搜寻doi结束。")
print(doi_list_for_citation_title_list)



# doi_list = ['10.1242/jeb.244461', '10.1111/ele.14160/v1/review2', '10.47119/ijrp1001171120234422', '10.1186/s40462-022-00361-2', '10.1007/s10661-022-10829-8', '10.1016/j.avrs.2022.100072', '10.1145/3491102.3502068', '10.1145/3512910', '10.1177/09567976211043425', '10.21203/rs.3.rs-34570/v1', '10.1109/access.2019.2904679', '10.31234/osf.io/cftes', '10.1016/j.ecocom.2022.101027', '10.1098/rsos.220859', '10.3390/d14121060', '10.1016/j.tree.2022.06.010', '10.1007/s10745-022-00320-w', '10.1016/j.envadv.2021.100161', '10.1093/obo/9780199830060-0057', '10.1007/978-3-030-58292-0_150175', '10.1186/s41235-021-00296-z', '10.1145/3478103', '10.1109/tse.2019.2931296', '10.1145/3471158.3472253', '10.1016/j.ijhcs.2021.102624', '10.1145/3411764.3445195', '10.1145/3396047', '10.1007/s42452-021-04162-x', '10.1109/tvcg.2020.3030443', '10.1016/j.cola.2020.101010', '10.1109/iri51335.2021.00025', '10.1007/978-3-030-72651-5_30', '10.1016/j.ipm.2020.102391', '10.1007/978-981-15-5148-2_21', '10.1007/978-3-030-58292-0_150175', '10.1007/s10816-021-09506-w', '10.1086/718141', '10.1145/3406865.3418371', '10.2139/ssrn.3657477', '10.1109/icsme46990.2020.00052', '10.1109/vl/hcc50065.2020.9127264', '10.1109/vl/hcc50065.2020.9127274', '10.1109/iri49571.2020.00014', '10.1016/j.chb.2020.106352', '10.1109/tcsvt.2019.2915103', '10.1016/j.apergo.2020.103102', '10.1016/j.ipm.2020.102241', '10.1145/3334480.3383025', '10.1080/10447318.2019.1646517', '10.1049/ic:19990888', '10.1007/978-3-030-61244-3_6', '10.1007/978-3-030-61244-3', '10.1007/s00521-020-05306-7', '10.1007/978-3-030-45688-7_43', '10.1007/978-3-030-45439-5_44', '10.1186/s40462-020-00213-x', '10.1145/3368567.3368583', '10.1109/cic48465.2019.00018', '10.3389/frobt.2019.00128', '10.1002/cpe.4342', '10.1109/vlhcc.2019.8818885', '10.1109/vlhcc.2019.8818795', '10.1109/vlhcc.2019.8818779', '10.1109/vlhcc.2019.8818850', '10.1007/s10791-019-09353-0', '10.1145/3341981.3344231', '10.1007/s10639-019-09921-3', '10.1016/j.cola.2019.04.003', '10.1145/3331184.3331379', '10.1145/3331184.3331398', '10.1016/j.jss.2019.04.028', '10.1016/j.dib.2019.103882', '10.1016/j.pmcj.2019.02.008', '10.1145/3289600.3290974', '10.1117/12.2518893', '10.1117/12.2592860', '10.2139/ssrn.4549843', '10.1371/journal.pone.0210423', '10.1093/acprof:oso/9780195173321.003.0001', '10.1016/b978-0-08-045337-8.00210-2', '10.1016/j.jhevol.2019.03.010', '10.1016/b978-0-12-809633-8.90160-2', '10.1109/tcsvt.2019.2915103', '10.1109/ccaa.2018.8777585', '10.1145/3279720.3279728', '10.1145/3272973.3274073', '10.1145/3236024.3275430', '10.1109/asonam.2018.8508811', '10.1109/vlhcc.2018.8506517', '10.1109/vlhcc.2018.8506526', '10.1177/0165551517713168', '10.1080/15230406.2017.1370391', '10.1177/1087054715616490', '10.1016/j.apergo.2018.01.010', '10.1145/3209978.3210027', '10.1080/10447318.2017.1368949', '10.2196/10507', '10.1145/3173574.3174136', '10.1080/10580530.2018.1440734', '10.1145/3172944.3172946', '10.1055/s-0038-1675179', '10.1515/9780804785747-003', '10.1016/j.cois.2018.02.002', '10.1007/s10745-018-0037-4', '10.1016/j.pubrev.2017.06.010', '10.1109/vlhcc.2017.8103447', '10.1109/vlhcc.2017.8103444', '10.1109/tem.2017.2722467', '10.25300/misq/2017/41.3.09', '10.1145/3106426.3106533', '10.1145/3077136.3080817', '10.1111/exsy.12414', '10.1109/bigdata.2017.8258509', '10.1016/j.jbi.2016.07.019', '10.2308/accr-51628', '10.1016/j.jbi.2017.01.007', '10.1080/10447318.2017.1278894', '10.1287/isre.2017.0695', '10.1145/3025453.3025818', '10.1016/j.inffus.2016.09.003', '10.1145/3020165.3022173', '10.1037/e524912015-106', '10.1016/j.cognition.2016.11.012', '10.1109/wi.2016.0065', '10.4324/9780203014349-13', '10.1007/978-3-319-25518-7_11', '10.1145/3106426.3106533', '10.2172/1481948', '10.1007/978-3-319-56535-4_41', '10.1007/s10668-016-9844-1', '10.14237/ebl.8.1.2017.786', '10.1016/j.jas.2017.01.001', '10.1016/j.seares.2016.08.004', '10.1080/07418825.2016.1244286', '10.1037/pspp0000165.supp', '10.3389/fpsyg.2016.01790', '10.1145/2993283.2993284', '10.1109/vlhcc.2016.7739675', '10.1109/vlhcc.2016.7739674', '10.1145/2950290.2950302', '10.1371/journal.pone.0161702', '10.1109/tcyb.2015.2420316', '10.1016/j.jbi.2016.03.023', '10.1145/2858036.2858469', '10.1037/pag0000079', '10.1007/s10916-015-0373-5', '10.18653/v1/w16-2923', '10.1037/e522172012-001', '10.13007/695', '10.7551/mitpress/10688.003.0003', '10.1117/12.2222805', '10.1109/wicom.2008.2046', '10.1111/j.1600-9657.2011.1025.x', '10.1093/acprof:oso/9780195173321.003.0004', '10.3389/fpsyg.2016.00017', '10.1007/s10916-015-0350-z', '10.1016/j.anbehav.2016.03.034', '10.1016/j.anbehav.2015.11.028', '10.1016/j.ppees.2016.02.004', '10.1890/15-1130.1', '10.1080/02602938.2014.991909', '10.1109/icsm.2015.7332447', '10.1109/icsm.2015.7332445', '10.1145/2808194.2809447', '10.1007/s10588-015-9185-x', '10.1145/2795235', '10.1145/2786567.2793688', '10.1145/2766462.2767874', '10.1111/tops.12149', '10.1111/tops.12147', '10.1037/e520602012-583', '10.1109/mcg.2015.50', '10.1109/vast.2014.7042552', '10.1016/j.promfg.2015.07.516', '10.1201/b18558-114', '10.1201/b18558-1', '10.1109/digitel.2008.10', '10.1007/978-3-319-19656-5_5', '10.1287/isre.2015.0581', '10.4018/978-1-4666-9562-7.ch092', '10.1111/exsy.12414', '10.1007/978-3-319-16486-1_25', '10.1007/978-1-4614-6825-7_16', '10.1073/pnas.1507637112', '10.1016/j.plrev.2015.05.001', '10.1108/jsit-01-2014-0003', '10.1145/2663714.2668049', '10.1145/2661829.2661904', '10.1145/2639189.2641202', '10.46895/lis.35.51', '10.1145/2637248.2637261', '10.1108/lht-01-2014-0011', '10.1098/rsif.2013.0859', '10.1109/urai34348.2014', '10.1109/urai.2014.7057373', '10.1080/00131857.2019.1631156', '10.1016/j.procs.2014.11.081', '10.1007/978-3-642-54516-0_13', '10.7554/elife.21883.052', '10.1016/j.bica.2014.11.003', '10.1007/978-3-319-13817-6', '10.1007/978-3-319-13817-6_1', '10.1007/978-3-319-13817-6_20', '10.1109/vlhcc.2014.6883009', '10.1109/vlhcc.2014.6883015', '10.1145/2637248.2637261', '10.1145/2637002.2637021', '10.1145/2637002.2637004', '10.1145/2609876.2609888', '10.1007/978-3-319-09891-3_53', '10.1007/978-3-319-14226-5_13', '10.1145/2591677', '10.1145/2615569.2615682', '10.1007/978-3-319-07854-0_20', '10.1007/3-540-29325-6_24', '10.1109/cogsima.2014.6816532', '10.1016/j.bica.2014.03.004', '10.1145/2556288.2557064', '10.1145/2531602.2531644', '10.1098/rspb.2013.2376', '10.1073/pnas.1408208111', '10.1109/vl/hcc51201.2021.9576420', '10.1109/vlhcc.2013.6645244', '10.1177/1541931213571052', '10.1155/2013/921695', '10.1109/icdm.2013.106', '10.1109/issrew.2013.6688890', '10.1515/9783110424164-toc', '10.1109/icse.2013.6606603', '10.37307/j.2194-1823.2005.33.05', '10.1109/cts.2013.6567241', '10.3390/admsci3030096', '10.1016/j.image.2012.07.002', '10.2304/elea.2013.10.2.116', '10.1145/2481492', '10.1145/2481492.2481499', '10.1111/j.1365-2729.2012.00491.x', '10.1145/2470654.2466418', '10.1145/2470654.2481415', '10.1145/2468356.2468419', '10.1117/12.2004735', '10.1109/mcg.2012.125', '10.1016/j.dss.2013.01.025', '10.1007/s12243-012-0316-9', '10.1016/j.tmp.2012.11.002', '10.1007/978-3-642-37015-1_39', '10.1145/2430545.2430551', '10.1109/tse.2010.111', '10.1016/c2011-0-07401-x', '10.1002/meet.14505001172', '10.1002/meet.14505001059', '10.1111/jcc4.12006', '10.1016/j.ipm.2012.03.001', '10.1016/j.compedu.2012.06.015', '10.2307/1941428', '10.1007/s10344-013-0729-4', '10.1109/wicsa-ecsa.212.22', '10.1109/wicsa-ecsa.212.5', '10.4018/jats.2012070104', '10.1145/1878537', '10.1109/bibmw.2012.6470309', '10.1037/a0026640', '10.1177/1473871612456122', '10.2753/mis0742-1222290207', '10.3389/fnhum.2012.00216', '10.12681/eadd/51362', '10.1177/1470593112441562', '10.1145/2207676.2208414', '10.1145/2207676.2208608', '10.1109/cogsima.2012.6188410', '10.1109/cogsima.2011.5753424', '10.1108/00330331211221837', '10.1093/acprof:oso/9780195374827.003.0022', '10.1145/2147783.2147788', '10.1201/b11433-92', '10.1016/j.dss.2011.09.006', '10.1016/j.chb.2011.08.008', '10.1016/j.ijhcs.2011.08.003', '10.1155/2012/364564', '10.1098/rsif.2011.0815', '10.1016/j.quaint.2011.04.024', '10.1145/2063576.2063649', '10.1109/vlhcc.2011.6070387', '10.1109/access.2017.2756069', '10.46354/i3m.2020.emss', '10.4018/jats.2012070104', '10.1115/detc2011-48238', '10.1109/culture-computing.2011.18', '10.3758/s13421-010-0068-6', '10.3030/101082636', '10.1145/2016904.2016907', '10.1186/1471-2296-12-90', '10.1007/978-3-642-21672-5_17', '10.1145/1985793.1985911', '10.1002/asi.21541', '10.1371/journal.pone.0021202', '10.1145/1978942.1979114', '10.1136/amiajnl-2011-000009', '10.1016/j.compenvurbsys.2011.01.003', '10.1007/978-3-642-17829-0_23', '10.1109/icsmc.2011.6084115', '10.1007/978-3-319-02264-2_12', '10.2307/23043491', '10.1111/j.1756-8765.2010.01128.x', '10.1093/beheco/arr038', '10.1016/j.ecss.2011.05.028', '10.5735/086.048.0406', '10.4103/0972-4923.86994', '10.1007/978-3-642-17155-0_3', '10.32657/10356/54872', '10.1111/j.1756-8765.2010.01128.x', '10.13182/t124', '10.13182/t124', '10.13182/t124', '10.1145/1937117.1937118', '10.1109/icbnmt.2010.5704879', '10.1145/1880071.1880138', '10.1109/vast.2010.5652895', '10.1109/simul17510.2010', '10.1109/simul.2010.9', '10.1109/icme.2010.5582595', '10.1109/devlrn.2010.5578859', '10.1109/tvcg.2010.177', '10.1145/1840784.1840805', '10.1145/3491102', '10.1145/3491102', '10.1145/3491102', '10.1145/3491102', '10.1145/1753326.1753332', '10.1145/1753846.1754088', '10.1109/hicss.2010.57', '10.5860/choice.45-1497', '10.1145/1880071.1880138', '10.2514/6.2023-0193.vid', '10.1145/1559845.1559959', '10.1145/1518701.1518705', '10.1145/1518701.1518795', '10.1145/1518701.1518796', '10.31219/osf.io/na3t7', '10.1016/j.dss.2013.01.025', '10.1109/kam.2009.42', '10.1109/vizsec.2009.5375542', '10.1007/978-3-642-04441-0', '10.1007/978-3-642-04636-0_24', '10.4324/9780203451199_chapter_7', '10.1109/ipcc.2009.5208668', '10.1007/978-3-642-03655-2_34', '10.1007/978-3-642-03655-2_49', '10.1007/978-3-642-02574-7_30', '10.1109/icpc.2009.5090040', '10.1177/1356766709335692', '10.1145/1520340.1520574', '10.1037/a0016995', '10.1016/j.joi.2009.03.004', '10.1111/j.1551-6709.2009.01020.x', '10.1109/tkde.2008.149', '10.1145/1518701.1518976', '10.1037/e578502012-005', '10.1007/978-3-642-04441-0_5', '10.1111/j.1467-8659.2009.01444.x', '10.1002/9781118983898.ch13', '10.1088/1751-8113/42/43/434002', '10.1016/j.jaa.2008.11.001', '10.1007/s10980-009-9333-0', '10.5860/choice.31-2685', '10.1145/1357054.1357207', '10.1145/1357054.1357261', '10.1109/vast.2008.4677373', '10.1109/vast.2008.4677362', '10.1109/vlhcc.2008.4639059', '10.5220/0002577102250233', '10.1177/016555150202800511', '10.3765/salt.v0i0.2888', '10.1109/icetet.2008.23', '10.1109/hicss.2008.191', '10.1016/j.ipm.2007.07.009', '10.1109/iwaise.2008.21', '10.1016/j.dss.2013.01.025', '10.1002/meet.2008.1450450332', '10.1086/528962', '10.21236/ada462156', '10.4018/978-1-59904-633-4.ch017', '10.4324/9780203402979-7', '10.1109/icit.2008.23', '10.1007/978-3-540-69423-6_36', '10.1109/wi.2007.80', '10.1109/vlhcc.2007.25', '10.1007/978-3-540-73257-0', '10.1109/tvcg.2007.70589', '10.1109/iv.2007.52', '10.1109/icimp.2007.8', '10.1145/3448748.3448777', '10.1037/0096-3445.136.3.370', '10.1016/j.ijhcs.2006.11.012', '10.1109/iat.2007.19', '10.1007/978-3-540-73257-0_7', '10.1145/1240866.1241063', '10.1080/01431160600954639', '10.1007/978-3-030-58292-0_150175', '10.3410/f.1086751.539665', '10.1145/1228175.1228249', '10.4018/978-1-59140-908-3.ch011', '10.1109/wsc.2006.323129', '10.1109/tse.2006.116', '10.1016/j.dss.2005.05.032', '10.1109/hicss.2006.71', '10.1109/tmm.2006.876294', '10.1145/1125170.1125241', '10.1002/asi.20249', '10.1016/j.tree.2005.11.021', '10.1006/tpbi.2000.1466', '10.1007/s00265-006-0187-z', '10.1007/11816102_7', '10.1016/j.beproc.2006.03.005', '10.4018/978-1-59140-309-8.ch007', '10.1515/9781937585006-toc', '10.1088/1742-6596/1842/1/012074', '10.1109/icme.2005.1521732', '10.1016/s0065-2830(05)29001-3', '10.1093/acprof:oso/9780195173321.003.0001', '10.1007/s10462-005-9008-4', '10.1108/02634500510589930', '10.1093/acprof:oso/9780195173321.003.0004', '10.1177/174498710501000406', '10.4018/978-1-5225-9279-2.ch011', '10.1145/3106426.3106533', '10.1007/3-540-32392-9_55', '10.1109/itcc.2004.1286468', '10.1109/itcc.2004.1286469', '10.1109/tkde.2004.1277818', '10.1007/978-3-540-27814-6_6', '10.2172/1164477', '10.2307/j.ctv36zrk6.11', '10.1016/j.ecolmodel.2003.10.022', '10.1016/j.anbehav.2004.03.003', '10.1016/j.jtbi.2003.10.013', '10.1145/765891.765961', '10.1145/957013.957109', '10.1145/889692.889699', '10.1145/642611.642699', '10.1145/606658.606660', '10.1145/3259365', '10.1016/b978-155860808-5/50007-1', '10.1007/3-540-44963-9_8', '10.1007/978-3-540-39850-9_5', '10.1145/957013.957045', '10.1002/mar.10097', '10.1016/s0040-5809(03)00012-1', '10.1145/1556262.1556272', '10.1145/506443.506635', '10.1145/506443.506635', '10.1145/584955.584962', '10.1016/s1071-5819(02)91015-3', '10.1145/544741.544847', '10.1127/entom.gen/26/2002/93', '10.1890/0012-9658(2002)083[1935:aoftta]2.0.co;2', '10.1034/j.1600-0706.2002.960121.x', '10.1145/634067.634167', '10.1145/564691.564768', '10.1089/10949310151088370', '10.1145/365024.365337', '10.1145/365024.365325', '10.1145/365024.365331', '10.1007/s11760-013-0587-2', '10.1093/wentk/9780190639440.003.0015', '10.1145/332040.332423', '10.1145/345513.345304', '10.2307/j.ctv36zrk6.5', '10.7551/mitpress/3120.003.0050', '10.1145/302979.303060', '10.1093/acprof:oso/9780195173321.003.0001', '10.1016/s0010-0277(99)00041-4', '10.1016/s1474-6670(17)38332-5', '10.1145/948496.948509', '10.1145/1133265', '10.4324/9781315777979-10', '10.1177/154193129804200503', '10.1145/288994.289003', '10.1145/276675.276746', '10.1145/274644.274650', '10.1145/286498', '10.1086/286113', '10.1007/bf00046328', '10.1002/(sici)1098-2361(1998)17:3<231::aid-zoo6>3.0.co;2-a', '10.1145/258549.258558', '10.1145/948449', '10.1109/ozchi.1996.560024', '10.1145/223904.223911', '10.1086/602724', '10.2307/3545484', '10.1093/beheco/3.3.211', '10.1007/bf00890430', '10.1007/bf02270709', '10.2307/3545394', '10.1086/204035', '10.1007/bf00046328', '10.2307/3545084', '10.7557/2.11.4.987', '10.1007/bf00889794', '10.3758/bf03197891', '10.1016/0022-247x(90)90397-x', '10.4319/lo.1989.34.1.0140', '10.1007/bf00378667', '10.1093/obo/9780199830060-0057', '10.1007/bf00888091', '10.1007/bf01047652', '10.2307/3565560', '10.1007/978-1-4613-1839-2_9', '10.1007/978-1-4613-1839-2_8', '10.1007/978-1-4613-1839-2_3', '10.1037/0097-7403.13.1.40', '10.1016/0162-3095(87)90055-0', '10.2307/1938669', '10.1093/acprof:oso/9780195173321.003.0001', '10.1525/aa.1986.88.1.02a00060', '10.1007/bf00889212', '10.1007/978-94-011-7918-8_3', '10.1093/obo/9780199830060-0057', '10.3354/meps027143', '10.2307/2802383', '10.1525/aa.1985.87.3.02a00100', '10.1017/s0140525x00020975', '10.1146/annurev.es.15.110184.002515', '10.1016/0040-5809(84)90029-7', '10.1037/0735-7036.98.2.142', '10.1086/203066', '10.1093/icb/23.2.291', '10.1525/aa.1983.85.3.02a00060', '10.1016/b978-0-12-505980-0.50014-8', '10.1007/bf00388069', '10.1093/obo/9780199830060-0057', '10.1016/b978-0-12-321250-4.50013-0', '10.1086/284235', '10.2307/2425376', '10.2307/3808435', '10.2307/3987', '10.1016/s0003-3472(82)80160-7', '10.1007/bf00889212', '10.1016/s0003-3472(81)80024-3', '10.1093/icb/21.4.813', '10.1007/bf00346824', '10.1016/s0003-3472(80)80003-0', '10.1086/409852', '10.1016/0040-5809(77)90046-6', '10.2307/2989628', '10.1086/283054', '10.2139/ssrn.4297941']
print("length of title:{}, and length of doi_list:{}".format(len(title_list), len(doi_list_for_citation_title_list)))
new_data = pd.DataFrame({'Title': title_list, 'DOI': doi_list_for_citation_title_list})
data = data.merge(new_data, on='Title', how='left')
data.to_excel("all_data.xlsx", index=False)
print("更新完成")
# doi_series = pd.Series(doi_list_for_citation_title_list)#转换为series好插入表格
# data['DOI'] = doi_series
# data.to_excel("citation_imp_updated.xlsx", index=False)