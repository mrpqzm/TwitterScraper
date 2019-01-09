loopCounter = 0
lastHeight = browser.execute_script("return document.body.scrollHeight")
while True:
    if loopCounter > 499:
        break # if the account follows a ton of people, its probably a bot, cut it off
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    newHeight = browser.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight:
        break
    lastHeight = newHeight

    
    
