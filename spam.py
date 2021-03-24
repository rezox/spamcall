#mau recode ijin dulu dong cape saya buatnya
#ijin nya ke telegram t.me/Xplt3
#klo gk ijin moga aja script nya rusak :v
#=========================================
import requests,json,os,time

os.system("clear")
banner = """
\t======================================
\t=         =  SPAM TELEPON =          =
\t======================================
\t=  [•]Creator : xplt3                =
\t=  [•]Telegram : t.me/Xplt3          =
\t=  [•]Bahasa : Python                =
\t=  [•]Example : 87*********          =
\t=  [•]Pesan : Gunakan dengan bijak   =
\t======================================
\t=    = Sederhana namun istimewa =    =
\t======================================
"""
print(banner)
nomor = input("\t[•] Nomor: ")

ua={
"Host":"id.jagreward.com",
"Connection":"keep-alive",
"Accept":"*/*",
"X-Requested-With":"XMLHttpRequest",
"sec-ch-ua-mobile":"?1",
"Save-Data":"on",
"User-Agent":"Mozilla/5.0 (Linux; Android 6; Oneplus One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
"Sec-Fetch-Site":"same-origin",
"Sec-Fetch-Mode":"cors",
"Sec-Fetch-Dest":"empty",
"Referer":"https://id.jagreward.com/member/register/",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
'Cookie':'PHPSESSID=jdsjb1lojb8fmn0ravo2uo8ktu; DAPROPS="sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:2|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _ga=GA1.3.2008028289.1616460336; _gid=GA1.3.267159521.1616460336'
}
url = f"https://id.jagreward.com/member/verify-mobile/{nomor}/"
req = requests.get(url,headers=ua).text
xplt = json.loads(req)
rs = xplt["result"] 
ms = xplt["message"] 
print()
print(f"Result: {rs}")
print()
print(f"Message: {ms}")
