PAGES     = 'https://www.lotteryusa.com/'
USA_PICK3 = 'https://www.lotteryusa.com/new-jersey/pick-3/'
USA_PICK4 = 'https://www.lotteryusa.com/new-jersey/pick-4/'

P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P3_NU1   = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
P3_NU2   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P3_NU3   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

P4_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

NEW_JERSEY_PM_LOTTERYUSA = {
    'URL' : [PAGES, USA_PICK3, USA_PICK4],
    'PICK3' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}

NEW_JERSEY_AM_TODO = [NEW_JERSEY_PM_LOTTERYUSA ]