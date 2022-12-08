#估值量化
##一个基本的定投模型
<br>从本堂课开始，我们就要真正进入量化定投的探索之旅，由一个最基本最简单的定投模型开始，一课一课的深入，最终找到那个可以指导我们实际操作的量化定投模型。
###§1从一个定投案例说起
<br>我们先来看一个基金定投的真实案例。
<br>一位家住上海的王女士，每月投入2000元，分别定投4只基金，每次投入500元----自2011年中旬定投开始的5年时间里，王女士始终不改初心，无论A股如何涨跌起伏，王女士都没有任何赎回行动，其定投记录堪称教科书式的基金定投。
<br>交易单据显示，王女士选择定投4只基金，并选择银行申购，其分别定投了广发核心精选、兴全有机增长、农银汇理增长和嘉实沪深300，王女士表示“这4只基金也是我做基金定投时，搞理财的朋友推荐给我的”。 朋友推荐应该是很多人买基金的“原动力”， 尤其是在牛市中你正好有一个在银行工作的朋友。
<br>具体来看，广发核心精选的对账单显示，王女士对该基金的定投始于2011年5月，每月均投入500元，直到2016年3月，累计投资59次，共动用资金2.95万元，截止2016年3月17日，王女士持有该基金15,739.5份，当日该基金单位净值为2.467元，其账面总资产为38,829.35元，账面浮盈为9329.35元，定投收益率为31.62%。
<br>同期开始定投的还有兴全有机增长，该基金总计投入也是2.95万元，截止2016年3月17日，王女士持有该基金20592.55份，当日该基金单位净值为2.5151元，其账面总资产为57192.32元，账面浮盈为22292.32元，定投收益率为75.56%。
<br>之后的2011年9月，王女士的定投组合又加入了农银汇理增长和嘉实沪深300两支基金。其中农银汇理增长的定投总次数为55次，总计投入为2.75万元，截止2016年3月17日，王女士持有该基金18818.83份，当日该基金单位净值为1.959元，其账面总资产为36866.09元，账面浮盈为9366.09元，定投收益率为34.05%。
<br>嘉实沪深300的定投总次数为55次，总计投入为2.75万元，截止2016年3月17日，王女士持有该基金37086.69分，当日该基金单位净值为0.8644元，其账面总资产为32057.73元，账面浮盈为4557.73元，定投收益率为16.57%。
<br>综上可知，自广发核心精选开始，王女士历经近5年的定投，总投入119400元，截止2016年3月17日的账面总资产为164945.49元，账面浮盈为45545元，定投收益率为39.95%，同样由于未在2015年高点时卖出，这份近5年的宛如教科书般的定投，其收益最终只有40%。
###§2构建一个基本的定投模型
<br>目前普通的定投都是针对基金而言的，基金公司为了本公司的利益会主动联合银行等渠道，给客户提供便捷化的定投服务，客户只需准备好一张银行卡，并保证在扣款日当天卡内余额高于扣款额即可。扣款额的多少可以由客户在签约时自由认定，少则200/300元，多则上千上万元。
案例中的王女士为了分散风险，选择了4支风格不同的基金进行定投，每月每支定投500元，坚持五年，风雨无阻，这种定投更加类似于“强制储蓄”。 从收益看，王女士的定投收益远远跑赢同期银行存款收益，勉强也算达到了其投资理财的目的。
<br>那么普通基金定投就可以定义为：每月在固定的时间买入固定金额的某支基金，其买入逻辑判断过程如下图所示，这个判断客户不用操心，都由银行和基金公司替客户完成了。
![processcn](./images/chapter2/processCN.png)
<br>显而易见，这是一个非常简单的定投模型，在此我将这个模型命名为模型一，模型一虽然简单，但是已经可以具备一个完整的量化交易系统的雏形了，我们对模型一定义如下：
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none">
 <tbody><tr>
  <td width="568" colspan="2" valign="top" style="width:426.1pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  </span><span style="font-family:宋体">模型一</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">买什么</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">上证指数</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">怎么买</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">每月最后一个交易日收盘价买入</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">买多少</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">2000</span><span style="font-family:宋体">元</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">怎么卖</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">无</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">卖多少</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">无</span></p>
  </td>
 </tr>
 <tr>
  <td width="73" valign="top" style="width:55.05pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span style="font-family:宋体">测试时间</span></p>
  </td>
  <td width="495" valign="top" style="width:371.05pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">2002.01.01-2016.12.30</span></p>
  </td>
 </tr>
</tbody></table>

###§3对模型一的说明
<br>下面就模型一涉及的问题作如下说明
<br>1.为何选择上证指数做测试
<br>众所周知，我们A股主板有两大交易所，分别为上海证券交易所和深圳证券交易所，两大交易所的代表指数为上证指数和深证综指，下图为上证指数全历史走势图。
![shang.png](./images/chapter2/shang.png)
<br>下图为深圳综指的全历史走势图。
![shen.png](./images/chapter2/shen.png)
<br>从上述图形中我们不难看出，2008年后，代表了一部分中小上市公司的深圳综指走势远远强于上证指数，如果我们用深综指这种过去大涨的指数来作为模型的测试样本，那么就有可能使我们的模型无法经受住大跌，大熊市的考验。
<br>我们必须对我们所测试的模型提出更加苛刻的测试条件，如果能在上证指数上赚钱，那么深圳综指一定不在话下，就好像能在大海中游泳的人，放在游泳池中一定没有问题，反之则可能会被海浪淹死。这一点请读者深入思考，当然之后我们依然会对深综指等主流指数进行测试，以证明模型的有效性。
<br>2.测试时间为何是2002.01.01-2016.12.30
<br>如果说前面选择上证指数就像选定一个战场的话，那么测试时间段的选择就好比给模型选一个好的“对手”， 一个最能体现出模型价值的对手。定投是一个长期的理财计划，时间短了肯定测不出来好坏，选单纯的上涨行情或者下跌行情也不行。A股的历史上有四次牛市行情，分别为2000年，2007年，2015年，2019年，能从中看出点规律吗？
很难，所以我们的测试时间段起码要有10年以上的时间。仔细观察上证指数，以2002~2016年这15年作为测试时间段还是很合适的，2000年之前的股市由于当时各方面条件并不成熟，参考价值比较小。所以我们最终选择了2002~2016年这个时间段。
<br>3.为何每月只买2000元
<br>定投金额的确定就比较主观了。一般来说，定投金额是和个人经济状况挂钩的，存款多收入高，定投金额当然水涨船高，在实际定投中，大家可以根据自己的情况酌情而定。
<br>我们做模型测试，考察模型的优劣基本都是用比例和参数，比如绝对收益率，年化收益率等等，这些数字和定投的绝对金额没有关系，所以不管我们设定定投金额是2000元也好还是5000元也罢，并不会有差别。
之所以选择2000元这个数字是因为绝大多数人的定投金额和此比较接近，计算出的结果大家从直观上更好理解。为了更好的做对比分析，本书以后所有的模型，大概率将年定投金额设定在2万元至3万元之间。
###§4模型一的测试
<br>至此，我们终于搞定了模型一中的细节问题了，下面开始测试。测试的过程就是模拟真实的交易过程，每次交易后把我们关心的几个数据记录下来，比如买卖金额，持有数量，盈利金额等等，这样就会形成一个长长的数据表。下图即是模型一的测试数据。单位：元
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="690" style="width:517.35pt;margin-left:-42.1pt;border-collapse:collapse;border:
 none">
 <tbody><tr style="height:27.0pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">时间</span></b></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal" style="margin-left:10.55pt;text-indent:-10.55pt"><b><span style="font-family:宋体">上</span> </b><b><span style="font-family:宋体">证</span></b></p>
  <p class="MsoNormal" style="margin-left:10.55pt;text-indent:-10.55pt"><b><span style="font-family:宋体">指</span> </b><b><span style="font-family:宋体">数</span></b></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">买卖</span><span lang="EN-US">&nbsp;
  </span></b><b><span style="font-family:宋体">金</span><span lang="EN-US">&nbsp;&nbsp;
  </span></b><b><span style="font-family:宋体">额</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">买卖份额</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">持有份额</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">市值</span></b></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">累计投</span><span lang="EN-US">&nbsp;&nbsp; </span></b><b><span style="font-family:宋体">入</span><span lang="EN-US">&nbsp; </span></b><b><span style="font-family:宋体">资</span><span lang="EN-US">&nbsp; </span></b><b><span style="font-family:宋体">金</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">总资产</span></b></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span style="font-family:宋体">盈利金额</span></b></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.49166</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1340.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1340.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">0.00 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.52469</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1311.74 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2652.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4044.29 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4044.29 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">44.29 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-03-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.6039</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1246.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3899.49 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">6254.39 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">6000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">6254.39 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">254.39 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.66774</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1199.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5098.72 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">8503.34 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">8000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">8503.34 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">503.34 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.51572</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1319.50 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">6418.22 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">9728.23 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">10000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">9728.23 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-271.77 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-06-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.73275</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1154.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">7572.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">13121.18 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">12000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">13121.18 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1121.18 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.65158</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1210.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">8783.42 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">14506.52 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">14000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">14506.52 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">506.52 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-08-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.66661</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1200.04 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">9983.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16638.53 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16638.53 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">638.53 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-09-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.58161</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1264.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">11247.99 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">17789.94 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">18000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">17789.94 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-210.06 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.50749</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1326.71 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">12574.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">18956.24 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">18956.24 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-1043.76 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-11-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.43417</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1394.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">13969.24 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20034.26 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">22000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20034.26 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-1965.74 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2002-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.35765</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1473.13 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">15442.37 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20965.34 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">24000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20965.34 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-3034.66 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-01-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.4998</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1333.51 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16775.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">25160.47 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">26000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">25160.47 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-839.53 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.51193</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1322.81 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">18098.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">27363.96 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">28000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">27363.96 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-636.04 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.51058</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1323.99 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">19422.69 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">29339.53 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">30000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">29339.53 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-660.47 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.52144</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1314.54 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">20737.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">31550.46 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">32000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">31550.46 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-449.54 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-05-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.57626</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1268.83 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">22006.06 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34687.27 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34687.27 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">687.27 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.48602</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1345.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">23351.94 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34701.45 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">36000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34701.45 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-1298.55 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.47674</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1354.33 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">24706.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">36484.74 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">38000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">36484.74 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-1515.26 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-08-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.42198</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1406.49 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">26112.76 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37131.82 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">40000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37131.82 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-2868.18 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.36716</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1462.89 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">27575.65 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37700.32 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">42000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37700.32 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-4299.68 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.3483</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1483.35 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">29059.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">39180.25 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">44000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">39180.25 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-4819.75 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-11-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.39722</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1431.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">30490.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">42601.81 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">46000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">42601.81 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-3398.19 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2003-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.49704</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1335.97 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">31826.38 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">47645.37 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">48000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">47645.37 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-354.63 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-01-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.59073</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1257.28 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">33083.67 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">52627.18 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">50000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">52627.18 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2627.18 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-02-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.67507</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1193.98 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">34277.65 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">57417.46 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">52000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">57417.46 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5417.46 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.74162</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1148.36 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">35426.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61698.63 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">54000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61698.63 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">7698.63 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.59559</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1253.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">36679.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">58525.37 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">58525.37 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2525.37 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.55591</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1285.42 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37964.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59069.93 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">58000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59069.93 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1069.93 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.39916</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1429.43 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">39394.31 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">55118.94 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">60000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">55118.94 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-4881.06 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-07-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.3862</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1442.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">40837.10 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56608.39 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56608.39 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-5391.61 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.34206</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1490.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">42327.35 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56805.84 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">64000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56805.84 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-7194.16 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.3967</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1431.95 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">43759.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61118.60 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">66000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61118.60 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-4881.40 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-10-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.32054</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1514.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">45273.83 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59785.90 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">68000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59785.90 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-8214.10 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.34077</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1491.68 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">46765.51 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62701.79 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">70000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62701.79 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-7298.21 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2004-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.2665</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1579.16 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">48344.66 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61228.51 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">72000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">61228.51 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-10771.49 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.19182</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1678.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">50022.77 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59618.13 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">74000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59618.13 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-14381.87 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.306</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1531.39 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">51554.16 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">67329.73 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">76000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">67329.73 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-8670.27 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.18124</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1693.14 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">53247.30 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62897.84 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">78000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62897.84 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-15102.16 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-04-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.15915</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1725.40 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">54972.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">63721.60 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">80000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">63721.60 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-16278.40 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.06074</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1885.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">56858.17 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">60311.74 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">82000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">60311.74 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-21688.26 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.0816</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1849.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">58707.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">63497.80 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">84000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">63497.80 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-20502.20 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-07-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.08303</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1846.67 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">60553.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">65581.75 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">86000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">65581.75 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-20418.25 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.1628</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1719.99 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62273.94 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">72412.14 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">88000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">72412.14 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-15587.86 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.15561</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1730.69 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">64004.63 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">73964.39 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">90000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">73964.39 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-16035.61 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.09282</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1830.13 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">65834.76 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">71945.54 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">92000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">71945.54 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-20054.46 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.09926</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1819.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">67654.16 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">74369.52 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">74369.52 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-19630.48 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2005-12-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.16106</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1722.56 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">69376.73 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">80550.54 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">96000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">80550.54 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-15449.46 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-01-25</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.25805</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1589.76 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">70966.49 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">89279.39 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">98000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">89279.39 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-8720.61 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.29903</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1539.61 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">72506.10 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94187.60 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">100000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94187.60 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-5812.40 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.2983</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1540.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">74046.58 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">96134.67 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">102000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">96134.67 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">-5865.33 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-04-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.44022</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1388.68 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">75435.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108643.36 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">104000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108643.36 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4643.36 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.6413</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1218.55 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">76653.80 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">125811.88 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">106000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">125811.88 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">19811.88 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.67221</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1196.02 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">77849.82 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">130181.25 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">130181.25 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">22181.25 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.61273</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1240.13 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">79089.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">127550.74 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">110000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">127550.74 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">17550.74 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.65864</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1205.81 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">80295.76 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">133181.76 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">112000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">133181.76 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">21181.76 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-09-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.75242</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1141.28 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">81437.04 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">142711.90 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">114000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">142711.90 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">28711.90 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.83799</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1088.15 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">82525.19 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">151680.47 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">116000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">151680.47 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">35680.47 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.09929</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">952.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">83477.89 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">175244.30 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">118000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">175244.30 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">57244.30 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2006-12-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.67547</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">747.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">84225.42 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">225342.59 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">120000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">225342.59 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">105342.59 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.78633</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">717.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">84943.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">236679.82 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">122000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">236679.82 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">114679.82 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.88107</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">694.19 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">85637.40 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">246727.34 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">124000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">246727.34 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">122727.34 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-03-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.18398</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">628.14 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">86265.54 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">274667.76 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">126000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">274667.76 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">148667.76 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.84127</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">520.66 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">86786.20 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">333369.24 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">128000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">333369.24 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">205369.24 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.10965</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">486.66 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">87272.86 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">358660.92 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">130000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">358660.92 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">228660.92 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-06-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.8207</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">523.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">87796.33 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">335443.43 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">132000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">335443.43 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">203443.43 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.47103</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">447.32 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">88243.65 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">394540.02 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">134000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">394540.02 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">260540.02 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5.21883</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">383.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">88626.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">462528.62 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">136000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">462528.62 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">326528.62 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-09-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5.5523</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">360.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">88987.09 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">494083.02 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">138000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">494083.02 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">356083.02 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5.95477</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">335.87 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">89322.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">531897.66 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">140000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">531897.66 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">391897.66 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.87178</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">410.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">89733.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">437161.79 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">142000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">437161.79 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">295161.79 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2007-12-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5.26156</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">380.12 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">90113.60 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">474138.11 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">144000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">474138.11 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">330138.11 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.38339</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">456.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">90569.87 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">397003.05 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">146000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">397003.05 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">251003.05 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-02-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.34854</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">459.92 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">91029.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">395846.69 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">148000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">395846.69 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">247846.69 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.47271</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">575.92 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">91605.71 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318120.07 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">150000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318120.07 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">168120.07 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.69311</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">541.55 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">92147.26 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">340309.96 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">152000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">340309.96 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">188309.96 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-05-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.43335</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">582.52 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">92729.78 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318373.79 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">154000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318373.79 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">164373.79 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.7361</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">730.97 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">93460.75 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">255717.95 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">156000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">255717.95 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">99717.95 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.77572</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">720.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94181.28 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">261420.87 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">158000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">261420.87 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">103420.87 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-08-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.39737</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">834.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">95015.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">227787.38 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">160000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">227787.38 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">67787.38 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-09-26</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.29378</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">871.92 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">95887.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">219944.72 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">162000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">219944.72 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">57944.72 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.72879</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1156.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">97044.33 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">167769.27 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">164000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">167769.27 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3769.27 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-11-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.87116</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1068.86 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">98113.19 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">183585.47 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">166000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">183585.47 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">17585.47 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2008-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.82081</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1098.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">99211.60 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">180645.47 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">168000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">180645.47 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">12645.47 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-01-23</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.99066</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1004.69 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">100216.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">199496.56 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">170000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">199496.56 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">29496.56 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-02-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.08285</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">960.22 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">101176.51 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">210735.50 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">172000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">210735.50 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">38735.50 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.37321</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">842.74 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">102019.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">242113.11 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">174000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">242113.11 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">68113.11 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.47757</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">807.24 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">102826.50 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">254759.84 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">176000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">254759.84 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">78759.84 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-05-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.63293</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">759.61 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">103586.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">272734.97 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">178000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">272734.97 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94734.97 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.95936</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">675.82 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">104261.93 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">308548.58 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">180000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">308548.58 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">128548.58 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.41206</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">586.16 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">104848.08 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">357747.96 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">182000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">357747.96 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">175747.96 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.66775</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">749.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">105597.78 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">281708.48 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">184000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">281708.48 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">97708.48 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.77943</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">719.57 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">106317.35 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">295501.64 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">186000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">295501.64 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">109501.64 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-10-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.99585</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">667.59 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">106984.94 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">320510.84 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">188000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">320510.84 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">132510.84 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.1953</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">625.92 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">107610.86 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343848.99 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">190000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343848.99 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">153848.99 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2009-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.27714</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">610.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108221.15 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">354655.86 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">192000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">354655.86 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">162655.86 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-01-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.98929</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">669.06 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108890.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">325504.40 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">194000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">325504.40 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">131504.40 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-02-26</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.05194</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">655.32 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">109545.53 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">334326.37 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">196000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">334326.37 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">138326.37 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.1091</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">643.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">110188.80 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">342587.99 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">198000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">342587.99 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">144587.99 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.87061</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">696.72 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">110885.51 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318309.07 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">200000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318309.07 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">118309.07 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.59215</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">771.56 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">111657.08 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">289431.89 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">202000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">289431.89 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">87431.89 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.39837</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">833.90 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">112490.97 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">269794.98 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">204000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">269794.98 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">65794.98 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-07-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.6375</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">758.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">113249.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">298694.95 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">206000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">298694.95 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">92694.95 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.6388</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">757.92 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">114007.19 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">300842.17 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">208000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">300842.17 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">92842.17 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.65566</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">753.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">114760.30 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">304764.33 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">210000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">304764.33 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">94764.33 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-10-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.97883</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">671.40 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">115431.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343851.42 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">212000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343851.42 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">131851.42 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.82018</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">709.17 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">116140.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">327538.18 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">214000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">327538.18 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">113538.18 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2010-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.80808</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">712.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">116853.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328132.87 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">216000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328132.87 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">112132.87 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.79069</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">716.67 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">117569.78 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328100.80 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">218000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328100.80 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">110100.80 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.90505</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">688.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">118258.23 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343546.08 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">220000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">343546.08 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">123546.08 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.92811</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">683.03 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">118941.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">348273.11 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">222000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">348273.11 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">126273.11 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-04-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.91151</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">686.93 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">119628.20 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">348298.69 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">224000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">348298.69 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">124298.69 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.74347</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">729.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">120357.20 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">330196.36 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">226000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">330196.36 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">104196.36 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.76208</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">724.09 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">121081.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">334436.21 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">228000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">334436.21 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">106436.21 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-07-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.70173</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">740.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">121821.56 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">329128.96 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">230000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">329128.96 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">99128.96 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.56734</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">779.02 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">122600.57 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">314757.36 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">232000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">314757.36 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">82757.36 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.35922</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">847.74 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">123448.31 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291241.73 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">234000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291241.73 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">57241.73 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.46825</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">810.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">124258.60 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">306701.30 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">236000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">306701.30 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">70701.30 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.33341</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">857.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">125115.72 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291946.27 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">238000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291946.27 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">53946.27 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2011-12-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.19942</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">909.33 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">126025.05 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">277182.01 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">240000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">277182.01 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">37182.01 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.29261</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">872.37 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">126897.42 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">290926.28 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">242000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">290926.28 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">48926.28 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-02-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.42849</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">823.56 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">127720.97 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310169.11 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">244000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310169.11 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">66169.11 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-03-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.26279</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">883.86 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">128604.84 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291005.74 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">246000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291005.74 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">45005.74 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-04-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.39632</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">834.61 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">129439.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310178.34 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">248000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310178.34 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62178.34 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.37223</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">843.09 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">130282.54 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">309060.15 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">250000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">309060.15 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59060.15 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-06-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.22543</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">898.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">131181.24 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291934.67 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">252000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">291934.67 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">39934.67 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.10363</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">950.74 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">132131.98 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">277956.80 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">254000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">277956.80 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">23956.80 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.04752</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">976.79 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">133108.77 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">272542.87 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">256000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">272542.87 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16542.87 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-09-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.08617</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">958.69 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">134067.47 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">279687.52 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">258000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">279687.52 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">21687.52 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.06888</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">966.71 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">135034.17 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">279369.50 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">260000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">279369.50 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">19369.50 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.98012</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1010.04 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">136044.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">269383.86 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">262000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">269383.86 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">7383.86 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2012-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.26913</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">881.40 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">136925.61 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310702.00 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">264000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310702.00 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">46702.00 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-01-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.38542</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">838.43 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">137764.03 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328625.08 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">266000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328625.08 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">62625.08 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.36559</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">845.46 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">138609.49 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">327893.22 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">268000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">327893.22 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">59893.22 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-03-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.23662</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">894.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">139503.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">312016.75 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">270000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">312016.75 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">42016.75 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-04-26</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.17791</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">918.31 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">140422.01 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">305826.49 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">272000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">305826.49 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">33826.49 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.30059</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">869.34 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">141291.35 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">325053.46 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">274000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">325053.46 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">51053.46 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-06-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.97921</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1010.50 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">142301.85 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">281645.25 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">276000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">281645.25 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">5645.25 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1.9938</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">1003.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">143304.96 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">285721.43 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">278000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">285721.43 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">7721.43 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-08-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.09838</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">953.12 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">144258.08 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">302708.27 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">280000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">302708.27 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">22708.27 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.17467</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">919.68 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">145177.76 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">315713.72 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">282000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">315713.72 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">33713.72 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.14161</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">933.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">146111.64 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">312914.14 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">284000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">312914.14 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">28914.14 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-11-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.2205</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">900.70 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">147012.33 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">326440.89 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">286000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">326440.89 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">40440.89 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2013-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.11598</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">945.19 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">147957.52 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">313075.16 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">288000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">313075.16 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">25075.16 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-01-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.03308</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">983.73 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">148941.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">302809.48 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">290000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">302809.48 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">12809.48 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-02-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.0563</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">972.62 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">149913.87 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">308267.90 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">292000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">308267.90 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">16267.90 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.03331</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">983.62 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">150897.49 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">306821.38 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">294000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">306821.38 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">12821.38 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.02636</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">986.99 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">151884.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">307772.64 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">296000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">307772.64 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">11772.64 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-05-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.03921</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">980.77 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">152865.25 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">311724.35 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">298000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">311724.35 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">13724.35 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.04833</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">976.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">153841.66 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">315118.48 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">300000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">315118.48 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">15118.48 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.20156</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">908.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">154750.11 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">340691.64 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">302000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">340691.64 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">38691.64 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-08-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.2172</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">902.04 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">155652.14 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">345111.93 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">304000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">345111.93 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">41111.93 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.36387</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">846.07 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">156498.21 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">369941.43 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">306000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">369941.43 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">63941.43 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.42018</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">826.38 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">157324.60 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">380753.85 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">308000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">380753.85 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">72753.85 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-11-28</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.68283</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">745.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">158070.08 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">424075.15 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">310000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">424075.15 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">114075.15 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2014-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.23468</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">618.30 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">158688.38 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">513306.13 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">312000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">513306.13 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">201306.13 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-01-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.21036</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">622.98 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">159311.36 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">511446.83 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">314000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">511446.83 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">197446.83 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-02-27</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.3103</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">604.17 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">159915.54 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">529368.40 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">316000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">529368.40 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">213368.40 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.7479</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">533.63 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">160449.17 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">601347.44 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">318000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">601347.44 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">283347.44 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-04-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.44166</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">450.28 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">160899.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">714660.66 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">320000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">714660.66 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">394660.66 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-05-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.61174</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">433.68 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">161333.13 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">744026.44 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">322000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">744026.44 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">422026.44 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">4.27722</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">467.59 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">161800.72 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">692057.28 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">324000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">692057.28 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">368057.28 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-07-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.66373</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">545.89 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">162346.61 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">594794.16 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">326000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">594794.16 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">268794.16 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.20599</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">623.83 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">162970.45 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">522481.62 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">328000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">522481.62 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">194481.62 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.05278</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">655.14 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">163625.59 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">499512.92 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">330000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">499512.92 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">169512.92 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-10-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.38256</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">591.27 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">164216.85 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">555473.36 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">332000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">555473.36 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">223473.36 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.4454</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">580.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">164797.34 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">567792.75 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">334000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">567792.75 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">233792.75 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2015-12-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.53918</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">565.10 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">165362.44 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">585247.44 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">336000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">585247.44 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">249247.44 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-01-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.7376</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">730.57 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">166093.01 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">454696.22 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">338000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">454696.22 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">116696.22 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-02-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.68798</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">744.05 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">166837.06 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">448454.68 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">340000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">448454.68 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">108454.68 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-03-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.00392</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">665.80 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">167502.86 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">503165.18 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">342000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">503165.18 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">161165.18 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-04-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.93832</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">680.66 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">168183.52 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">494177.00 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">344000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">494177.00 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">150177.00 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-05-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.91662</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">685.73 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">168869.24 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">492527.41 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">346000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">492527.41 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">146527.41 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-06-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.92961</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">682.68 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">169551.93 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">496721.02 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">348000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">496721.02 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">148721.02 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-07-29</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2.97934</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">671.29 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">170223.22 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">507152.84 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">350000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">507152.84 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">157152.84 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-08-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.08549</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">648.20 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">170871.41 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">527222.04 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">352000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">527222.04 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">175222.04 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-09-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.0047</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">665.62 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">171537.04 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">515417.34 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">354000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">515417.34 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">161417.34 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-10-31</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.10049</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">645.06 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">172182.10 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">533848.87 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">356000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">533848.87 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">177848.87 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-11-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.25003</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">615.38 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">172797.48 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">561596.98 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">358000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">561596.98 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">203596.98 </span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2016-12-30</span></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">3.10364</span></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">2000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">644.40 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">173441.88 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">538301.16 </span></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">360000.00 </span></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">538301.16 </span></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><span lang="EN-US">178301.16 </span></p>
  </td>
 </tr>
</tbody></table>

<br>对于这个测试数据做如下解释：
<br>1. 上面的表格展示了15年内每次定投日当天账户的买卖情况和资金状态，大家能够非常清楚无误的看到模型的运行情况，篇幅虽长，但是很重要。
<br>2. 表中的上证即是上证指数，为了计算方便，我们将上证指数都除以1000，比如2016年12月30日的上证指数是3103.64点，除以1000在模型计算中就是3.10364。
<br>3. 表格中买卖份额数有小数的存在，但是实际我们真实的买卖份额数都是100的整数倍，这样处理是为了模型计算的方便，比如2016年12月30日这次买入操作，买入金额2000元，指数点位3.10364，那么买入的数量是644.40份，实际中我们只能买入600份，二者的买入金额相差137.82元。
这种误差如果做四舍五入的处理，那么买入金额有的月份超过2000元有的少于2000元，整体看这样的处理并不会对模型的有效性产生显著影响。
###§5模型一的分析
<br>面对茫茫的数字，很多人估计会头疼，这该怎么分析呢？我们先来抽丝拨茧，进行一步步的分析，大家自然就会明白模型一的表现究竟如何。
<br>首先看一下，模型一的投入资金、总资产和盈利资金走势图。
![three1.png](./images/chapter2/three1.png)
<br>图中的棕色线表示我们定投累计投入的本金，由于我们每月固定买入2000元，所以它是一根有固定斜率笔直向上的直线，紫色曲线代表我们持有的资产的总市值，由于没有卖出操作，总市值等于总资产，金色曲线是模型一的盈利资金曲线。
<br>在定投的头4个年头，由于指数的持续下跌，模型一并不能帮我们赚钱，还在亏钱。这个时期是积累期，我们不知道何时会盈利，但是未来终会迎来牛市，从紫色曲线和棕色线的关系看，模型一的亏损比率并不大。
从整个图形看，紫色曲线绝大多数时间运行在棕色线上方。这说明，经过数年的定投，模型一是一个“正收益”系统。即便在以后的熊市中，依然能保证我们至少在股市最熊的时候不亏钱。
金色曲线呢，在2007年牛市最巅峰时，模型一能盈利40万，这可是一笔巨款啊！但是随后的2008年和2014年，模型一也能让这笔巨款大部分统统还给市场，非常的不理想啊！
<br>有了上面的感性认识，我们下面看看模型一的分年统计表：
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="632" style="width:473.85pt;margin-left:4.65pt;border-collapse:collapse">
 <tbody><tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span style="font-size:10.0pt;font-family:宋体">年份</span></b></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">每年投<span lang="EN-US">&nbsp;&nbsp;&nbsp;
  </span>入本金</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">累计投<span lang="EN-US">&nbsp;&nbsp;&nbsp;
  </span>入本金</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">总资产</span></b></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">盈利金额</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">绝对收益率</span></b></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-bottom:solid #B1E388 1.0pt;background:white;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">年化收益率</span></b></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2002-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">20965.34
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-3034.66
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-12.64%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-12.64%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2003-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">48000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">47645.37
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-354.63
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-0.74%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-0.49%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2004-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">72000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">61228.51
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-10771.49
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-14.96%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-7.89%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2005-12-30</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">96000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">80550.54
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-15449.46
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-16.09%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-6.90%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2006-12-29</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">120000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">225342.59
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">105342.59
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">87.79%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">21.80%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2007-12-28</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">144000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">474138.11
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">330138.11
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">229.26%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">35.42%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2008-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">168000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">180645.47
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">12645.47
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">7.53%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">1.81%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2009-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">192000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">354655.86
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">162655.86
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">84.72%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">13.55%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2010-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">216000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">328132.87
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">112132.87
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">51.91%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">8.27%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2011-12-30</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">240000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">277182.01
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">37182.01
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">15.49%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2.60%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2012-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">264000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">310702.00
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">46702.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">17.69%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2.69%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2013-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">288000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">313075.16
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">25075.16
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">8.71%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">1.28%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2014-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">312000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">513306.13
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">201306.13
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">64.52%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">6.90%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2015-12-31</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">336000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">585247.44
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">249247.44
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">74.18%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">7.13%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2016-12-30</span></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">360000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">538301.16
  </span></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">178301.16
  </span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:solid windowtext 1.0pt;border-bottom:solid windowtext 1.0pt;
  border-right:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">49.53%</span></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-top:none;background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">4.88%</span></p>
  </td>
 </tr>
</tbody></table>

<br>数字虽然枯燥，但是却能更加精确的描述我们的感性认识。
<br>（1）	从投入资金看。每年匀速固定投入2.4万元，就像强制存款一样。到2016年底期末共投入36万元。从15年这么一个长期的跨度看，这个数额对于普通家庭是合适的。
<br>（2）	从盈利金额看。模型一有两个盈利的高峰，一个在2007年，14.4万的本金盈利达到33万。一个在2015年6月。32万的本金盈利42万元。2015年之所以盈利比较低。原因就是2015年上证指数不如2007年那么牛，6月底指数在4400点，而2007年却达到了6124点。
<br>（3）	从绝对收益率看。定投开始了4个年头，模型一一直在亏损。2005年底，亏损达到16%。虽然亏损让人不爽，但是我们要看到，这4年上证指数的跌幅达到22.16%。
有低谷当然就有高潮，在定投的第6年底，模型一共投入14.4万元的本金，而总资产飙升到了47万多，绝对收益率达到了229.27%，2010年后上证开始慢慢熊途。模型一获利金额几乎回吐完毕，但是却一直保持不亏损。在之后的2015年牛市行情中，再次上演王者归来的好戏。
<br>（4）	从年化收益率看。说到年化收益率，大家可不要小看这个指标。我们的定投模型，资金并不是一股脑的一次性投入。而是分散在每月投入，用绝对收益率这个指标看，模型一的收益率才为49.53%。不明就里的吃瓜群众可能会说，弄了15年才赚这么点儿，你炒的是股票吗？
但是你们仔细想想，那么评价模型一公平吗？显然我们需要一个真正能衡量资金持续流入模型的盈利评价指标。这样我们就必须使用年化收益率指标。为了大家能更直观的理解，我们用一个例子来解释。
<br>小王第1年年初投入100元做生意，到了第1年年末没赚钱，第2年不再投入。到了第2年年末，小王赚了100元，到了第2年年末，小王总共有200元。小王这100元本金在这两年里的年化收益率就是41.42%。可以算一算，100*1.4142*1.4142=200。也就是说这100元每年都相当于带来了41.42%的收益。
更进一步，假如小王第2年年初再追加投入资金50元，到了第2年年末依然赚100元。第2年年末，小王的总资产就是250元。这回小王的年化收益率就是35.08%。计算如下：（100*1.3508+50）*1.3508=250。在实际应用中，我们使用电子表格软件中的IRR函数可以很方便地计算出年化收益率。
###§6模型一的探讨
<br>过上述例子，我们再回过头来看模型一的期末年化收益率4.88%。这个4.88%意味着过去15年我们每月投入的每一笔钱，从投入的那一刻起，都在享受每年高达4.88%的收益，一直到2016年底测试结束。看到这里估计有些朋友会说这就是复利呀，对，复利，爱因斯坦说过，复利是世界第八大奇迹。
这几年比较火爆的银行理财产品，给出的年化利率也就4%~5%，如此简单的模型就能让我们轻松享受到银行理财产品的收益率。而且我们要认识到2016年12月底，上证指数3100点左右，这个位置并不高。在2015年6月上证涨到5100点时，模型一的年化收益率可是达到了12%。
在那时如果我们选择全身而退的话，这个收益率基本就能达到民间借贷的水平了。如果在那时别人叫你一声股神，估计你会非常受用。但是仔细想想我们炒股了吗？我们买了指数，但是我们没炒，我们更像是在理财在投资。
设想一下，当一个想理财的小白走进基金公司的大门时，一个热情的推销员把这个财富故事讲给他听，小白会不会怦然心动呢？但在兴奋之余，我们应该冷静的看到模型一头4年亏损，直到2013年底定投12年后，年化收益率才1.28%，它连银行定期存款都不如的尴尬。
<br>分析到这里，大家一定对模型一有了比较透彻的了解。模型一的特点是不择时，也就是说不管指数高低每月都买。但是我们知道指数在高位时买入并长期持有的话，亏损的比例还是很大的。所以很多人说定投的起点很重要，从低位开始定投，当然长期看很爽，但是如果从高位开始定投，那岂不是悲剧了？
比如拿模型一来说，如果定投的起点不是2002年1月，而是2007年10月呢？从最高点6100点开始定投，这应该算是最惨的开始了吧。下图是2007年10月到2016年12月的上证指数K线图。
![shang2007](./images/chapter2/shang2007.png)
测试的过程这里就不再展示，我们直接来看看结果吧。
![three2](./images/chapter2/three2.png)
<br>看看棕色线和紫色线的关系，是不是觉得不可思议呢？不要怀疑自己的眼睛，模型一到期末并未赔钱，甚至还有一些利润呢，看下表。
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="615" style="width:461.45pt;margin-left:4.65pt;border-collapse:collapse">
 <tbody><tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="left" style="text-align:left"><b><span style="font-size:10.0pt;font-family:宋体">年份</span></b></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">每年投<span lang="EN-US">&nbsp; </span>入本金</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">累计投<span lang="EN-US">&nbsp;&nbsp; </span>入本金</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">总资产</span></b></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">盈利金额</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">绝对收益率</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span style="font-size:10.0pt;font-family:宋体">年化收益率</span></b></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2007-12-28</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">6000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">6000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">5927.19
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-72.81
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-1.21%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-1.21%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2008-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">30000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">18616.89
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-11383.11
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-37.94%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-33.49%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2009-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">54000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">63032.70
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">9032.70
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">16.73%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">9.60%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2010-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">78000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">78250.00
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">250.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">0.32%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">0.15%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2011-12-30</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">102000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">81462.02
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-20537.98
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-20.14%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-8.34%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2012-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">126000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">108778.73
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-17221.27
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-13.67%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-4.65%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2013-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">150000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">124780.25
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-25219.75
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-16.81%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">-5.05%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2014-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">174000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">225461.37
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">51461.37
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">29.58%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">6.25%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2015-12-31</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">198000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">270306.11
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">72306.11
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">36.52%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  background:#E6F5D8;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">6.67%</span></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  border-top:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">2016-12-30</span></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">24000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">222000.00
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">262117.26
  </span></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">40117.26
  </span></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">18.07%</span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="right" style="text-align:right"><span lang="EN-US" style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;;color:black">3.22%</span></p>
  </td>
 </tr>
</tbody></table>

<br>上证指数2007年10月到2016年12月，跌幅是47.9%，而模型一同期的绝对收益率是18.07%年，化收益率更是达到3.22%。虽然我们错过了2002~2007年的最大牛市，而且从最惨的最高点开始定投，但是年化收益率真的还可以。从上述两个测试，我们能认识一个事实：当定投的时间达到一定的长度后，定投的起点就可能不再重要。
这一事实可能会颠覆很多人原有的认识，之前有很多高手在不断的教育我们，低点开始的投资很重要，从高位定投和从低位定投差异很大。不能说这种观点就完全错误，也不能说它就不全面，资本市场中就是这样，没有绝对的对和错，我们需要的是理性的判断。
读到这里，相信大家应该仔细回想一下自己过去这几年炒股的历程，套牢的经历。我们付出了多少的时间和精力，还有金钱，但是我们做的有没有比模型一的效果更好呢？
<br>模型一作为最基础的定投模型，我们用真实的回测数据验证了其“强大”的赚钱能力，但是我们肯定不会仅仅满足于此。在2007年指数6000点和2015年指数5000点时，模型一还在买入，当我们用“后视镜”看，在如此高的点位还在买，肯定是不理想的。
在指数的高位能否暂停买入呢？是的，我们必须做到这一点。那么问题来了，如何判断指数处于高位还是低位呢？在下一堂课我们将送给大家一把“尺子”，一把能衡量指数处于高位还是低位的“尺子”。








