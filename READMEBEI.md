#Valuationquan
##Chapter 2
A Basic Fixed Investment Model
From this lesson, we will really enter the exploration journey of quantitative investment, starting with a basic and simple fixed investment model, and finally find the quantitative fixed investment model that can guide our actual operation.
###§1starting from a case of fixed investment
<br>Let's first look at a real case of fund fixed investment.
<br>Ms. Wang, who lives in Shanghai, invests 2000 yuan each month in four funds, and 500 yuan each time. During the five years since the beginning of the fixed investment in the middle of 2011, Ms. Wang has never changed her mind. 
<br>No matter how the A shares rise and fall, Ms. Wang has not taken any redemption action, and her fixed investment record can be regarded as a textbook fund fixed investment.
<br>According to the transaction documents, Ms. Wang chose to invest in four funds and chose the bank to apply for purchase. She invested in GF Core Selective Equity, Xingquan Organic Growth, ABC-CA Growth Equity and Harvest CSI 300 respectively. 
<br>Ms. Wang said that "these four funds were also recommended to me by my friends engaged in financial management when I made fund investment". A friend's recommendation should be the "driving force" for many people to buy funds, especially in a bull market when you happen to have a friend who works in a bank.
<br>Specifically, the selected statement of GF Core Selective shows that Ms. Wang's fixed investment in the fund started in May 2011, with an average of 500 yuan invested every month. 
<br>Until March 2016, she has invested 59 times, with a total of 29500 yuan. As of March 17, 2016, Ms. Wang held 15739.5 shares of the fund. On that day, the net value of the fund unit was 2.467 yuan, the total book assets was 38829.35 yuan, the book floating profit was 9329.35 yuan, and the fixed investment yield was 31.62%.
<br>She also started its fixed investment in Xingquan Organic Growth in the same period. The total investment of the fund was also 29500 yuan. As of March 17, 2016, Ms. Wang held 20592.55 shares of the fund. On that day, the net value of the fund unit was 2.5151 yuan. 
<br>Its total book assets were 57192.32 yuan, book floating profit was 22292.32 yuan, and the fixed investment yield was 75.56%.
<br>Later, in September 2011, Ms. Wang added two funds, ABC-CA Growth Equity and Harvest CSI 300, to her fixed investment portfolio.
<br>Among them, the total number of fixed investments increased by ABC-CA Growth Equity was 55, with a total investment of 27500 yuan. As of March 17, 2016, Ms. Wang held 18818.83 shares of the fund. 
<br>On that day, the unit net value of the fund was 1.959 yuan, its total book assets was 36866.09 yuan, its book floating profit was 9366.09 yuan, and the rate of return on fixed investments was 34.05%.
<br>The total number of fixed investments of Harvest CSI 300 was 55, with a total investment of 27500 yuan. As of March 17, 2016, Ms. Wang held 37086.69 shares of the fund. On that day, the net value of the fund unit was 0.8644 yuan. Its total book assets were 32057.73 yuan, book floating profit was 4557.73 yuan, and the fixed investment yield was 16.57%.
<br>To sum up, since the GF Core Selection, Ms. Wang has invested 119400 yuan in fixed investment for nearly five years. As of March 17, 2016, the total book asset was 164945.49 yuan, the book floating profit was 45545 yuan, and the fixed investment yield was 39.95%.
<br>Also, because she did not sell at the peak in 2015, this fixed investment for nearly five years was like a textbook, and its yield was only 40%.
###§2build a basic fixed investment model
<br>Now, the common fixed investment is for the fund. For the benefit of the company, the fund company will actively cooperate with banks and other channels to provide customers with convenient fixed investment services. 
<br>Customers only need to prepare a bank card and ensure that the balance in the card on the day of deduction is higher than the amount deducted. The amount of deduction can be freely determined by the customer when signing the contract, ranging from 200/300 yuan to tens of thousands of yuan.
<br>In order to spread the risk, Ms. Wang in the case chose four funds with different styles to make a fixed investment of 500 yuan each month for five years. This kind of fixed investment is more similar to "forced savings". 
<br>From the perspective of income, Ms. Wang's fixed investment income far outperformed the bank deposit income in the same period, and barely achieved her investment and financing purpose.
<br>Then this type of fixed investment can be defined as: buying a certain fund with a fixed amount at a fixed time every month. The buying logic judgment process is shown in the following figure. The customers need not worry about this judgment. The banks and fund companies complete it for the customers.
<br>
<br>Obviously, this is a very simple fixed investment model. Here I name this model Model 1. Although Model 1 is simple, it can already have the prototype of a complete quantitative trading system. We define Model 1 as follows:
<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none'>
 <tr>
  <td width=568 colspan=2 valign=top style='width:426.1pt;border:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  Model 1</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>Buy what</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>Shanghai stock exchange composite index</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>How to buy</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>buy at the closing price on the last
  trading day of each month</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>How much</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>2000 yuan</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>How to sell</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>nothing</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>How much</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>nothing</span></p>
  </td>
 </tr>
 <tr>
  <td width=83 valign=top style='width:62.1pt;border:solid windowtext 1.0pt;
  border-top:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>Test time</span></p>
  </td>
  <td width=485 valign=top style='width:364.0pt;border-top:none;border-left:
  none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal><span lang=EN-US>&nbsp;</span></p>
  </td>
 </tr>
</table>