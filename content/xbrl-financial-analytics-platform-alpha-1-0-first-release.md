Title: XBRL Financial Analytics Platform (Alpha 1.0): First release
Date: 2012-12-25 19:19
Author: namitkewat
Category: XBRL
Tags: financial analytics, python, python xbrl, xbrl, xbrl analytics, XBRL Financial Analytics, xbrlfinapp
Slug: xbrl-financial-analytics-platform-alpha-1-0-first-release
Status: published

Hello friends,

Today i am releasing first alpha release of my xbrl analytics platform.

Its URL is: <http://xbrlfinapp.pythonanywhere.com/>

Its a web application, targeting users whose XBRL is on SEC/or not on
SEC/or not in public domain yet/or anyone who is interested in XBRL data
and want to do the financial analytics.

At present it is only working for US-GAAP TAXONOMY VERSIONS 09,11,12.

Website's layout and design is simple; just upload valid zipped xbrl
package and see the result on Homepage only. Upload file size has limit
of 5MB. If you want to increase that limit then please show me that
xbrl.

Limited numbers of financial formulas(Key performance Indicators) have
been included; because current website design and hosting type is
restricting them. But these formulas are using data from XBRL package
only; no access  to market information(like; share price).

Well, all those improvements are in progress.

This app represents final analysed data in form of table;similar how
arelle is loading xbrl file. But its not. It is doing complex algorithm
of data finding.

For example; consider two cases as; 1st: " Correctly determining what
total equity is if an SEC filer does not provide total equity" 2nd:
"Correctly determining what total revenues is when the filer does not
provide total revenues or when they use obscure concepts to express
revenues"

Lets take this challenge to my app; first download one xbrl filling from
SEC from
[here](http://www.sec.gov/Archives/edgar/data/63754/000006375412000005/0000063754-12-000005-xbrl.zip "here") and
upload it to xbrlfinapp application.

case 1. Filler has not provided total equity
concept("us-gaap\_StockholdersEquity"); and my application has find out
its three components, they
are: RetainedEarningsAccumulatedDeficit,  CommonStockValue,  AccumulatedOtherComprehensiveIncomeLossNetOfTax.

case 2. Filler has not provided 'total revenues'
concept('us-gaap\_Revenues'); and then in such case my application has
find out its two components, they are; InterestExpense,  SalesRevenueNet

Similarly filler has not provided 'Pre-Tax Income Loss'
concept('us-gaap\_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest');  
and then my application has find out its two components, they are;<span
style="color:#333333;font-family:verdana, arial, sans-serif;"> </span>IncomeLossFromEquityMethodInvestments,  IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments.  
Other cases like; filer has not provided 'Total Costs and Expenses'
concept (us-gaap\_CostsAndExpenses) and then my application has find out
its five components
as; InterestExpense, CostOfGoodsSold, OtherPostretirementBenefitExpense, SellingGeneralAndAdministrativeExpense, PensionExpense.

 

but Current Assets(us-gaap\_AssetsCurrent),Current
liabilities(us-gaap\_LiabilitiesCurrent), Total
Assets(us-gaap\_Assets) ,Operating Income
Loss(us-gaap\_OperatingIncomeLoss) are present; so they are not
recalculated again.

By this way; you can upload any xbrl package from SEC(under UGT version
09,11,12).

 

[![Screen shot 2012-12-24 at 9.21.29
PM](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-24-at-9-21-29-pm.png "Home Page")](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-24-at-9-21-29-pm.png)
[![Screen shot 2012-12-24 at 9.22.10
PM](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-24-at-9-22-10-pm.png "Home page after uploading and showing result")](http://namitkewat.files.wordpress.com/2012/12/screen-shot-2012-12-24-at-9-22-10-pm.png)

Also there might be some bug or error in doing analysis; if you find
them then please inform me at 'namitkewat@gmail.com'
