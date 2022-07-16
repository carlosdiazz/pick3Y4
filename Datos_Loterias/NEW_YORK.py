NY_AM_PAGES     = 'https://www.lotteryusa.com/'
NY_AM_PICK3 = 'https://www.lotteryusa.com/new-york/midday-numbers/'
NY_AM_PICK4 = 'https://www.lotteryusa.com/new-york/midday-win-4/'

NY_PM_PAGES     = 'https://www.lotteryusa.com/'
NY_PM_PICK3 = 'https://www.lotteryusa.com/new-york/numbers/'
NY_PM_PICK4 = 'https://www.lotteryusa.com/new-york/win-4/'

NY_P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_P3_NU1   = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_P3_NU2   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_P3_NU3   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

NY_P4_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
NY_P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

NEW_YORK_LOTTERYUSA = {
    'URL_MIDDAY' : [NY_AM_PAGES, NY_AM_PICK3, NY_AM_PICK4],
    'PICK3_MIDDAY' : [NY_P3_FECHA,NY_P3_NU1,NY_P3_NU2,NY_P3_NU3 ],
    'PICK4_MIDDAY' : [NY_P4_FECHA,NY_P4_NU1,NY_P4_NU2,NY_P4_NU3,NY_P4_NU4 ],
    'URL_EVENING' : [NY_AM_PAGES, NY_AM_PICK3, NY_AM_PICK4],
    'PICK3_EVENING' : [NY_P3_FECHA,NY_P3_NU1,NY_P3_NU2,NY_P3_NU3 ],
    'PICK4_EVENING' : [NY_P4_FECHA,NY_P4_NU1,NY_P4_NU2,NY_P4_NU3,NY_P4_NU4 ]
}

NEW_YORK_TODO = [NEW_YORK_LOTTERYUSA ]