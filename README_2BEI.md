#Valuationquan
##Chapter 2
A Basic Fixed Investment Model
From this lesson, we will really enter the exploration journey of quantitative investment, starting with a basic and simple fixed investment model, and finally find the quantitative fixed investment model that can guide our actual operation.
###§1starting from a case of fixed investment
<br>Let's first look at a real case of fund fixed investment.
<br>Ms. Wang, who lives in Shanghai, invests 2000 yuan each month in four funds, and 500 yuan each time. During the five years since the beginning of the fixed investment in the middle of 2011, Ms. Wang has never changed her mind. 
No matter how the A shares rise and fall, Ms. Wang has not taken any redemption action, and her fixed investment record can be regarded as a textbook fund fixed investment.
<br>According to the transaction documents, Ms. Wang chose to invest in four funds and chose the bank to apply for purchase. She invested in GF Core Selective Equity, Xingquan Organic Growth, ABC-CA Growth Equity and Harvest CSI 300 respectively. 
Ms. Wang said that "these four funds were also recommended to me by my friends engaged in financial management when I made fund investment". A friend's recommendation should be the "driving force" for many people to buy funds, especially in a bull market when you happen to have a friend who works in a bank.
<br>Specifically, the selected statement of GF Core Selective shows that Ms. Wang's fixed investment in the fund started in May 2011, with an average of 500 yuan invested every month. 
Until March 2016, she has invested 59 times, with a total of 29500 yuan. As of March 17, 2016, Ms. Wang held 15739.5 shares of the fund. On that day, the net value of the fund unit was 2.467 yuan, the total book assets was 38829.35 yuan, the book floating profit was 9329.35 yuan, and the fixed investment yield was 31.62%.
<br>She also started its fixed investment in Xingquan Organic Growth in the same period. The total investment of the fund was also 29500 yuan. As of March 17, 2016, Ms. Wang held 20592.55 shares of the fund. On that day, the net value of the fund unit was 2.5151 yuan. 
Its total book assets were 57192.32 yuan, book floating profit was 22292.32 yuan, and the fixed investment yield was 75.56%.
<br>Later, in September 2011, Ms. Wang added two funds, ABC-CA Growth Equity and Harvest CSI 300, to her fixed investment portfolio.
<br>Among them, the total number of fixed investments increased by ABC-CA Growth Equity was 55, with a total investment of 27500 yuan. As of March 17, 2016, Ms. Wang held 18818.83 shares of the fund. 
On that day, the unit net value of the fund was 1.959 yuan, its total book assets was 36866.09 yuan, its book floating profit was 9366.09 yuan, and the rate of return on fixed investments was 34.05%.
<br>The total number of fixed investments of Harvest CSI 300 was 55, with a total investment of 27500 yuan. As of March 17, 2016, Ms. Wang held 37086.69 shares of the fund. On that day, the net value of the fund unit was 0.8644 yuan. Its total book assets were 32057.73 yuan, book floating profit was 4557.73 yuan, and the fixed investment yield was 16.57%.
<br>To sum up, since the GF Core Selection, Ms. Wang has invested 119400 yuan in fixed investment for nearly five years. As of March 17, 2016, the total book asset was 164945.49 yuan, the book floating profit was 45545 yuan, and the fixed investment yield was 39.95%.
Also, because she did not sell at the peak in 2015, this fixed investment for nearly five years was like a textbook, and its yield was only 40%.
###§2build a basic fixed investment model
<br>Now, the common fixed investment is for the fund. For the benefit of the company, the fund company will actively cooperate with banks and other channels to provide customers with convenient fixed investment services. 
Customers only need to prepare a bank card and ensure that the balance in the card on the day of deduction is higher than the amount deducted. The amount of deduction can be freely determined by the customer when signing the contract, ranging from 200/300 yuan to tens of thousands of yuan.
In order to spread the risk, Ms. Wang in the case chose four funds with different styles to make a fixed investment of 500 yuan each month for five years. This kind of fixed investment is more similar to "forced savings". 
From the perspective of income, Ms. Wang's fixed investment income far outperformed the bank deposit income in the same period, and barely achieved her investment and financing purpose.
<br>Then this type of fixed investment can be defined as: buying a certain fund with a fixed amount at a fixed time every month. The buying logic judgment process is shown in the following figure. The customers need not worry about this judgment. The banks and fund companies complete it for the customers.
![process](images/chapter2/process.png)
<br>Obviously, this is a very simple fixed investment model. Here I name this model Model 1. Although Model 1 is simple, it can already have the prototype of a complete quantitative trading system. We define Model 1 as follows:
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" style="border-collapse:collapse;border:none">
 <tbody><tr>
  <td width="568" colspan="2" valign="top" style="width:426.1pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Model 1</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Buy what</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Shanghai Stock Exchange composite index</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">How to buy</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">buy at the closing price on the last
  trading day of each month</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">How much</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">2000 yuan</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">How to sell</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">nothing</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">How much</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">nothing</span></p>
  </td>
 </tr>
 <tr>
  <td width="83" valign="top" style="width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">Test time</span></p>
  </td>
  <td width="485" valign="top" style="width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt">
  <p class="MsoNormal"><span lang="EN-US">2002.01.01-2016.12.30</span></p>
  </td>
 </tr>
</tbody></table>
###§3instructions for model 1
<br>The problems involved in model 1 are described as follows:
<br>1.	Why choose Shanghai Stock Exchange Index for testing?
<br>As we all know, there are two major exchanges on the A-share main board, Shanghai Stock Exchange and Shenzhen Stock Exchange,the representative indexes of the two exchanges are the Shanghai Composite Index and the Shenzhen Composite Index. The chart below shows the overall historical trend of the Shanghai Composite Index.
![shang](images/chapter2/shang.png)
<br>The chart below shows the overall historical trend of Shenzhen Composite Index.
![shen](images/chapter2/shen.png)
<br>From the above graph, we can easily see that after 2008, the Shenzhen Composite Index represents the trend of some small and medium-sized listed companies,It is far stronger than the Shanghai Stock Exchange Index.
If we use the Shenzhen Composite Index, which has risen sharply in the past, as the test sample of the model, it may make our model unable to withstand the test of the sharp decline and big bear market.
<br>We must put forward more stringent test conditions for the model we are testing. If we can make money on the Shanghai Stock Exchange Index,so the Shenzhen Composite Index must be easy. 
Just like people who can swim in the sea, it must be OK to put them in the swimming pool, otherwise they may be drowned by the waves. Please think deeply about this. Of course, we will still test the Shenzhen Composite Index and other mainstream indexes to prove the effectiveness of the model.
<br>2.	Why is the test time from January 1, 2002 to December 30, 2016?
<br>If the previous selection of the SSE index is like selecting a battlefield, then the selection of the test period is like choosing a good "opponent" who can best reflect the value of the model. Fixed investment is a long-term financial management plan.
It will not be good or bad if the time is short. It is not good to choose a simple upward or downward market. There have been four bull markets in the history of A-share, respectively in 2000, 2007, 2015 and 2019.
Can you see some rules from them? It's very difficult, so our testing period should be at least 10 years. Carefully observe the Shanghai Stock Exchange Index.
It is appropriate to take the 15 years from 2002 to 2016 as the test period. The stock market before 2000 was not mature in all aspects at that time, so the reference value was relatively small. we finally chose the period from 2002 to 2016.
<br>3.	Why only buy 2000 yuan per month
<br>The determination of fixed investment amount is subjective. Generally speaking, the fixed investment amount is related to the personal economic situation, and who have many deposits,with high income, the amount of fixed investment will certainly increase. In actual fixed investment, you can decide according to your own situation.
<br>We do model testing, and we basically use proportions and parameters to evaluate the merits of the model, such as absolute rate of return, annualized rate of return, etc. These figures have nothing to do with the absolute amount of fixed investment, so no matter whether we set the fixed investment amount to be 2000 yuan or 5000 yuan, there will be no difference. 
The reason for choosing the figure of 2000 yuan is that the fixed investment amount of most people is close to this, and the calculated result is intuitively better understood. 
In order to make a better comparative analysis, the annual fixed investment amount of all future models in this book is roughly set between 20000 yuan and 30000 yuan.
###§4testing for model 1
<br>So far, we have finally solved the details in Model 1, and now we begin to test. The process of testing is to simulate the real transaction process. After each transaction, we will record several data we care about, such as purchase and sale amount, holding amount, profit amount, etc., which will form a long data table. 
The following figure shows the test data of Model 1.                                                                                                  Unit: yuan(RMB)
<table class="MsoTableGrid" border="1" cellspacing="0" cellpadding="0" width="690" style="width:517.35pt;margin-left:-42.1pt;border-collapse:collapse;border:
 none">
 <tbody><tr style="height:27.0pt">
  <td width="80" nowrap="" valign="top" style="width:60.0pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Time</span></b></p>
  </td>
  <td width="67" nowrap="" valign="top" style="width:50.6pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Shanghai</span></b></p>
  <p class="MsoNormal"><b><span lang="EN-US">Stock index</span></b></p>
  </td>
  <td width="65" nowrap="" valign="top" style="width:48.85pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">B/S&nbsp; amount</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">B/S&nbsp; shares</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Holding</span></b></p>
  <p class="MsoNormal"><b><span lang="EN-US">shares</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Market</span></b></p>
  <p class="MsoNormal"><b><span lang="EN-US">value</span></b></p>
  </td>
  <td width="91" nowrap="" valign="top" style="width:67.9pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Accumulated investment</span></b></p>
  </td>
  <td width="76" nowrap="" valign="top" style="width:2.0cm;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Total</span></b></p>
  <p class="MsoNormal"><b><span lang="EN-US">asserts</span></b></p>
  </td>
  <td width="84" nowrap="" valign="top" style="width:63.2pt;border:solid windowtext 1.0pt;
  border-left:none;padding:0cm 5.4pt 0cm 5.4pt;height:27.0pt">
  <p class="MsoNormal"><b><span lang="EN-US">Profit amount</span></b></p>
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
The test data is explained as follows:
<br>1. The above table shows the trading and capital status of the account on each investment day in 15 years. You can see the operation of the model clearly and accurately. Although it is long, it is important.
<br>2. The Shanghai Index in the table is the Shanghai Stock Exchange Index. For the convenience of calculation, we divide the Shanghai Stock Exchange Index by 1000. For example, the Shanghai Stock Exchange Index on December 30, 2016 is 3103.64 points, and dividing by 1000 is 3.10364 for model calculation.
<br>3. There are decimals in the number of buying and selling shares in the table, but the actual number of buying and selling shares is an integral multiple of 100. This processing is for the convenience of model calculation. For example, in the purchase operation on December 30, 2016, the purchase amount was 2000 yuan, and the index point was 3.10364, so the number of purchased shares was 644.40. 
In fact, we can only buy 600 shares, and the difference between the two purchase amounts was 137.82 yuan. If the difference is rounded, the purchase amount may exceed 2000 yuan or be less than 2000 yuan in some months. On the whole, such treatment will not have a significant impact on the effectiveness of the model.
###§5analysis for model 1
<br>In the face of vast numbers, many people are expected to have headaches. How should we analyze this? Let's draw the cocoon and analyze it step by step, and you will naturally understand the performance of Model 1.
<br>First, let's take a look at the trend chart of investment capital, total assets and profit capital of Model I.
![three2](images/chapter2/three1.png)
<br>The brown line in the figure represents the accumulated principal of our fixed investment. Since we regularly buy 2000 yuan every month, it is a straight line with a fixed slope. The purple curve represents the total market value of the assets we hold. Since there is no selling operation, the total market value is equal to the total assets. The gold curve is the profit amount curve of Model 1.
<br>In the first four years of fixed investment, due to the continuous decline of the index, the model could not help us make money and was still losing money. This period is an accumulation period. We don't know when we will get a profit, but a bull market will come in the future. 
From the relationship between the purple curve and the brown line, the loss ratio of model 1 is not large. From the whole graph, the purple curve runs above the brown line most of the time. This shows that after years of fixed investment, Model 1 is a "positive return" system. Even in the future bear market, we can still guarantee that we will not lose money at least when the stock market is at its worst. 
As for the golden curve, at the peak of the bull market in 2007, the model made a profit of 400,000, which was a huge sum of money! However, in the following years of 2008 and 2014, Model 1 also allowed most of this huge sum to be returned to the market, which was not ideal!
<br>With the above perceptual knowledge, let's take a look at the annual statistical table of Model 1:
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="632" style="width:474.1pt;margin-left:4.65pt;border-collapse:collapse">
 <tbody><tr style="height:14.1pt">
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><b><span lang="EN-US" style="font-size:10.0pt">date</span></b></p>
  </td>
  <td width="89" nowrap="" valign="bottom" style="width:66.6pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">investment per year</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">accumulated investment</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">total assets</span></b></p>
  </td>
  <td width="95" nowrap="" valign="bottom" style="width:70.9pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">profit amount</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:solid windowtext 1.0pt;
  border-left:solid windowtext 1.0pt;border-bottom:solid #B1E388 1.0pt;
  border-right:none;background:white;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">absolute RR</span></b></p>
  </td>
  <td width="92" nowrap="" valign="bottom" style="width:69.1pt;border:solid windowtext 1.0pt;
  border-bottom:solid #B1E388 1.0pt;background:white;padding:0cm 5.4pt 0cm 5.4pt;
  height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">annualized RR</span></b></p>
  </td>
 </tr>
 <tr style="height:14.1pt">
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
  <td width="83" nowrap="" valign="bottom" style="width:62.0pt;border-top:none;
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
Although the numbers are boring, they can more accurately describe our perceptual knowledge.
<br>(1)	From the perspective of investment funds. A fixed investment of 24000 yuan at a constant amount every year, just like compulsory deposit. By the end of 2016, a total of 360000 yuan had been invested. From a long-term span of 15 years, this amount is suitable for ordinary families.
<br>(2)	In terms of profit amount. There are two profit peaks in Model 1. In 2007, the principal profit of 144,000 yuan reached 330,000 yuan. One in June 2015. The principal profit of 320000 yuan is 420000 yuan. In 2015, the profit was relatively low. The reason is that the Shanghai Stock Exchange Index in 2015 was not as good as that in 2007. At the end of June, the index was at 4400 points, while in 2007 it reached 6124 points.
<br>(3)	In terms of absolute rate of return. The fixed investment has started for four years, and Model 1 has been losing money. At the end of 2005, the loss reached 16%. Although the loss is unpleasant, we should see that the Shanghai Stock Exchange Index has dropped by 22.16% in the past four years.
There is certainly a climax when there is a trough. At the end of the sixth year of the fixed investment, the model invested a total of 144000 yuan in principal, while the total assets soared to more than 470000, with an absolute yield of 229.27%.
After 2010, Shanghai market began to bear slowly. For the model 1, the profit amount has almost been taken back, but it has been kept without loss. Later, in the bull market of 2015, the return of the king was staged again.
<br>(4)	From the perspective of annualized rate of return. When it comes to annualized rate of return, we should not underestimate this indicator. In our fixed investment model, capital is not a one-time investment. Instead, it is distributed in the monthly investment.
Using the absolute rate of return as an indicator, the rate of return of model 1 is 49.53%. The unknown melon eaters may say that it took 15 years to earn such a little. Are you speculating in stocks? But when you think about it, evaluation model 1 like this is fair?
Obviously, we need a profit evaluation index that can truly measure the continuous capital inflow model. In this way, we must use annualized yield indicators. For a more intuitive understanding, let's use an example to explain.
<br>Ms. Wang invested 100 yuan in business at the beginning of the first year, but did not make money at the end of the first year, and did not invest in the second year. At the end of the second year, Ms. Wang earned 100 yuan.
At the end of the second year, Ms. Wang had 200 yuan in total. The annualized yield of Ms. Wang's 100 yuan principal in the past two years is 41.42%. It can be calculated, 100 * 1.4142 * 1.4142=200. 
That is to say, the 100 yuan is equivalent to 41.42% of the income every year. Further, if Ms. Wang invests 50 yuan more at the beginning of the second year, she will still earn 100 yuan by the end of the second year. 
At the end of the second year, Ms. Wang's total assets were 250 yuan. This time, Ms. Wang's annualized yield is 35.08%. The calculation is as follows: (100 * 1.3508+50) * 1.3508=250. In practical application, we can easily calculate the annualized rate of return by using the IRR function in the spreadsheet software.
###§6discussion on Model 1
<br>Through the above example, we can look back at the year-end annualized yield of 4.88% in Model 1. This 4.88% means that every amount of money we invested every month in the past 15 years has enjoyed an annual income of up to 4.88% from the moment of investment until the end of 2016. It is estimated that some friends will say that this is compound interest. 
Yes, compound interest. Einstein said that compound interest is the eighth miracle in the world. For the popular bank financial products in recent years, the annual interest rate is only 4%~5%. Such a simple model allows us to easily enjoy the yield of bank financial products. 
And we should realize that at the end of December 2016, the Shanghai Composite Index was about 3100 points, which was not high. When the Shanghai Stock Exchange rose to 5100 points in June 2015, the annualized yield of Model 1 reached 12%. 
At that time, if we choose to withdraw, the yield will basically reach the level of private lending. If someone called you a stock god at that time, you would be very useful. But do you think that it is stock speculation? 
We bought the index, but we didn't speculate. We are more like financing and investing. Imagine that when Xiaobai, who wants to manage money, walks into the door of a fund company, and a passionate salesman tells him the wealth story, will Xiaobai be thrilled? 
But when we are excited, we should calmly see that the model has lost money in the first four years. The annualized yield was only 1.28% 12 years after the fixed investment at the end of 2013, which is not even as good as the bank fixed deposit.
<br>At this point, we must have a thorough understanding of Model 1. Model 1 is characterized by no timing, that is, buying every month regardless of the index. But we know that if the index is bought at a high level and held for a long time, the proportion of losses is still large. 
So many people say that the starting point of the investment is very important. Of course, it's good to start investment from the low position in the long run. But if you start investment from the high position, wouldn't it be a tragedy?
Take Model 1 for example. What if the starting point of fixed investment is not January 2002, but October 2007? Starting from the highest point of 6100, this should be the worst start. The following figure is the K line chart of the Shanghai Stock Exchange Index from October 2007 to December 2016.
![shang2007](images/chapter2/shang2007.png)
<br>The testing process will not be shown here. Let's just look at the results.
![three2](images/chapter2/three2.png)
<br>Isn't it amazing to see the relationship between the brown line and the purple line? Don't doubt your own eyes. The model has not lost money at the end of the period, and even has some profits. See the table below.
<table class="MsoNormalTable" border="0" cellspacing="0" cellpadding="0" width="615" style="width:461.45pt;margin-left:4.65pt;border-collapse:collapse">
 <tbody><tr style="height:14.1pt">
  <td width="82" nowrap="" valign="bottom" style="width:61.75pt;border:solid windowtext 1.0pt;
  background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal"><b><span lang="EN-US" style="font-size:10.0pt">date</span></b></p>
  </td>
  <td width="79" nowrap="" valign="bottom" style="width:59.5pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">investment per year</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">accumulated investment</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">total assets</span></b></p>
  </td>
  <td width="104" nowrap="" valign="bottom" style="width:77.95pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">profit amount</span></b></p>
  </td>
  <td width="85" nowrap="" valign="bottom" style="width:63.8pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">absolute RR</span></b></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border:solid windowtext 1.0pt;
  border-left:none;background:#7FD13B;padding:0cm 5.4pt 0cm 5.4pt;height:14.1pt">
  <p class="MsoNormal" align="center" style="text-align:center"><b><span lang="EN-US" style="font-size:10.0pt">annualized RR</span></b></p>
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
From October 2007 to December 2016, the Shanghai Stock Exchange Index fell by 47.9%, while the absolute yield of the same period of the model was 18.07%, and the converted yield reached 3.22%. 
Although we missed the biggest bull market from 2002 to 2007, and started to make a decision from the worst peak, the annualized returns were quite straightforward. From the above two tests, we can recognize the fact that the starting point of the fixed investment may not be important when the fixed investment time reaches a certain length.
This fact may overturn the original understanding of many people. Many experts have been educating us constantly before. Investment starting from the low point is very important. There is a big difference between making a decision from a high position and making a decision from a low position.
It cannot be said that this view is completely wrong or incomplete. This is the case in the capital market. There is no absolute right or wrong. What we need is rational judgment. After reading this, I believe you should carefully reflect on your own experience in the past few years. How much time, energy and money have we paid, but have we done better than Model 1?
<br>As the most basic fixed investment model, Model 1 has verified its "strong" earning ability with real back test data, but we will certainly not be satisfied with this. When the index was 6000 points in 2007 and 5000 points in 2015, the model was still buying. 
When we used the "rearview mirror" to see, it was certainly not ideal to still buy at such a high point. Can we stop buying at the high level of the index? Yes, we must do that. 
Then the question arises, how to judge whether the index is in a high or low position? In the next chapter, we will give you a "ruler", a "ruler" that can measure whether the index is high or low.