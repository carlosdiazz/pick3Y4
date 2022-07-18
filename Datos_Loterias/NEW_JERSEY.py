NJ_AM_PAGES     = 'https://www.lotteryusa.com/'
NJ_AM_PICK3 = 'https://www.lotteryusa.com/new-jersey/midday-pick-3/'
NJ_AM_PICK4 = 'https://www.lotteryusa.com/new-jersey/midday-pick-4/'

NJ_PM_PAGES     = 'https://www.lotteryusa.com/'
NJ_PM_PICK3 = 'https://www.lotteryusa.com/new-jersey/pick-3/'
NJ_PM_PICK4 = 'https://www.lotteryusa.com/new-jersey/pick-4/'

P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P3_NU1   = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
P3_NU2   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P3_NU3   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

P4_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

NEW_JERSEY_LOTTERYUSA = {

    'URL_MIDDAY' : [NJ_AM_PAGES, NJ_AM_PICK3, NJ_AM_PICK4],
    'PICK3_MIDDAY' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_MIDDAY' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ],

    'URL_EVENING' : [NJ_PM_PAGES, NJ_PM_PICK3, NJ_PM_PICK4],
    'PICK3_EVENING' : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3 ],
    'PICK4_EVENING' : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4 ]
}

NEW_JERSEY_TODO = [NEW_JERSEY_LOTTERYUSA ]