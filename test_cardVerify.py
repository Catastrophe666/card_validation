import cardVerify

def test_validateName():
    assert cardVerify.validateName("Akash")==True
    assert cardVerify.validateName("Maria")==True
    assert cardVerify.validateName("9tgfsh")==False
    assert cardVerify.validateName("Aka76")==False
    
def sum_digit():
    assert cardVerify.sum_digits(2)==2
    assert cardVerify.sum_digits(9)==9
    assert cardVerify.sum_digits(11)==2
    assert cardVerify.sum_digits(13)==4

def test_validateCvv():
    assert cardVerify.validateCvv("314")==True
    assert cardVerify.validateCvv("615")==True
    assert cardVerify.validateCvv("91")==False
    assert cardVerify.validateCvv("1")==False
    
def test_lunh_algo():
    assert cardVerify.lunh_algo("61789372994")==True
    assert cardVerify.lunh_algo("49927398716")==True
    assert cardVerify.lunh_algo("49927398717")==False
    assert cardVerify.lunh_algo("1234567812345678")==False

def test_validateExpiry():    
    assert cardVerify.validateExpiry("09/21")==True
    assert cardVerify.validateExpiry("03/25")==True
    assert cardVerify.validateExpiry("09/12")==False
    assert cardVerify.validateExpiry("09/03")==False

def test_checkCardValidity():
    assert cardVerify.checkCardValidity("Akanksha","79927398713","343","03/22")==True
    assert cardVerify.checkCardValidity("Adarsh","79927391134","51","04/23")==False
    assert cardVerify.checkCardValidity("Kar3tik","79927391134","113","03/27")==False
    assert cardVerify.checkCardValidity("Pruthvi","79927391134","823","03/03")==False

