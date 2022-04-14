from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time

def selenium_get(zh,mm,num,pingjia):

    web = Chrome()

    web.get('https://jpv2-2.mycospxk.com/wx/ver2.28.1/index.html?v=2.28.1#/user/login?universitycode=10579')

    time.sleep(1)

    web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div/div[2]/div/div[2]/input').send_keys(f'{zh}') #账号密码

    web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div/div[3]/div/div[2]/input').send_keys(f'{mm}')

    time.sleep(1)

    web.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]').click() #点击登录
    time.sleep(3)
    web.find_element_by_xpath('//*[@id="homelayout"]/div/div[3]/div[1]').click() #点进评价问卷
    time.sleep(2)
    # web.find_element_by_xpath('//*[@id="BasicLayout__contentBody___qwde2"]/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div').click() #点进评价问卷
    # time.sleep(2)
    count = 1
    while(count<=num):
        time.sleep(2)
        try:
            for i in range(46,56):
                sli_ele = web.find_element_by_xpath(f'// *[ @ id = "{i}"]').send_keys(Keys.BACK_SPACE*3)
                sli_ele = web.find_element_by_xpath(f'// *[ @ id = "{i}"]').send_keys('9.99')
            web.find_element_by_xpath('//*[@id="57"]/label[1]/span[1]/input').click()

            web.find_element_by_xpath('//*[@id="56"]').send_keys(f'{pingjia}')
            web.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[6]/form/div/div[16]/button').click()
            time.sleep(2)
            # if(web.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div/span')):
            #     web.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div/div/div/div/span').click()
            # // *[ @ id = "am-modal-container-1639360716875"] / div / div[2] / div / div / div / div / div / span
            count+=1
        except Exception as e:
            break
            print("评价已经完毕，若还有没有评价的问卷可以再运行一次")
    web.quit()

if __name__ == '__main__':
    print("注意：使用前请下载chorme浏览器，并确保chorme版本号为99.0.xxxx.xx！！！")
    print("使用说明：\n1.使用脚本前请先进行校园网认证;\n2.如果没登进去请检查自己的网络跟账号密码;\n3.脚本默认给满分，如果不想所有老师都给满分，就先评价完那位老师的问卷再run脚本;\n4.如果一个科目有两位老师执教可能需要run两遍脚本，小bug")
    print('\t'*10+"———20CSkuku")
    pingjia = input("写下你对每一位老师的同样的评价:")
    zh = input('输入用户名:')
    mm = input('输入密码:')
    num=30
    # pingjia = '教学质量很棒！'
    selenium_get(zh,mm,num,pingjia)