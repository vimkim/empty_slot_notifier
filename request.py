html = driver.execute_script("""return document.getElementsByTagName('frame')['firstF'].contentDocument.getElementsByTagName('frame')["ILec"].contentDocument.getElementsByTagName('table')[0].innerHTML""")
f = open('output.html', 'w')
f.write(html)

