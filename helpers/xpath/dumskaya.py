#main
enter_button = '//a[@id="pp"]/b'
registration_button = '//a[@href="/register/"]'

#registration
email_field = '//input[@name="email"]/following::input[@name="email"]'
nick_field = '//input[@name="nick"]'
password_field = '//input[@name="password1"]'
password2_field = '//input[@name="password2"]'
male_radio = '//input[@value="m"]'
female_radio = '//input[@value="f"]'
finish_button = '//input[@type="submit"]/following::input[@type="submit"]'

#user page
user_name_label = '//a[@class="celluname1"]'

#Materials
first_article = '//div[@id="articles"]/descendant::div[1]/a[1]'
materials_button = '//div[@class="menutable"]/descendant::div[1]/a[1]'

class Home:
    enter_button = '//a[@id="pp"]/b'
    registration_button = '//a[@href="/register/"]'

class Registration:
    email_field = '//input[@name="email"]/following::input[@name="email"]'
    nick_field = '//input[@name="nick"]'
    password_field = '//input[@name="password1"]'
    password2_field = '//input[@name="password2"]'
    male_radio = '//input[@value="m"]'
    female_radio = '//input[@value="f"]'
    finish_button = '//input[@type="submit"]/following::input[@type="submit"]'

class User:
    user_name_label = '//a[@class="celluname1"]'