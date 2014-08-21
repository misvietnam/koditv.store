#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.htvonline'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
if 5 - 5: iiI / ii1I
def ooO0OO000o ( ) :
 ii11i = "http://api.htvonline.com.vn/tv_channels"
 oOooOoO0Oo0O = '{"pageCount":200,"category_id":"-1","startIndex":0}'
 iI1 = i1I11i ( ii11i , oOooOoO0Oo0O )
 for OoOoOO00 in iI1 [ "data" ] :
  I11i = OoOoOO00 [ "link_play" ] [ 0 ] [ "resolution" ]
  O0O = OoOoOO00 [ "image" ]
  Oo = "%s (%s)" % ( OoOoOO00 [ "intro_text" ] , I11i )
  I1ii11iIi11i ( Oo . encode ( "utf8" ) , OoOoOO00 [ "id" ] . encode ( "utf8" ) , "playvideo" , O0O )
  if 48 - 48: oO0o / OOooOOo / I11iIi1I / IiiIII111iI
 try :
  IiII = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  #IiII = xbmc . translatePath ( os . path . join ( IiII , "temp.jpg" ) )
  #urllib . urlretrieve ( 'http://echipstore.net/images/htvonline.jpg' , IiII )
  #iI1Ii11111iIi = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiII )
  #i1i1II = xbmcgui . WindowDialog ( )
  #i1i1II . addControl ( iI1Ii11111iIi )
  #i1i1II . doModal ( )
 finally :
  pass
  if 96 - 96: o0OO0 - Oo0ooO0oo0oO . I1i1iI1i - o00ooo0 / o00 * Oo0oO0ooo
 o0oOoO00o = xbmc . getSkinDir ( )
 if o0oOoO00o == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 43 - 43: O0OOo . II1Iiii1111i
def i1IIi11111i ( cid , title ) :
 ii11i = "http://api.htvonline.com.vn/tv_channels"
 oOooOoO0Oo0O = '{"pageCount":200,"category_id":"-1","startIndex":0}'
 iI1 = i1I11i ( ii11i , oOooOoO0Oo0O )
 for OoOoOO00 in iI1 [ "data" ] :
  print 'cid = %s - channel["id"] = %s' % ( cid , OoOoOO00 [ "id" ] . encode ( "utf8" ) )
  if OoOoOO00 [ "id" ] . encode ( "utf8" ) == cid :
   o000o0o00o0Oo = OoOoOO00 [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
   print o000o0o00o0Oo
   oo = xbmcgui . ListItem ( title )
   oo . setInfo ( 'video' , { 'Title' : title } )
   oo . setProperty ( "IsPlayable" , "true" )
   oo . setPath ( o000o0o00o0Oo )
   xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , oo )
   if 33 - 33: I1I1i1 * oO0 / OOo0o0 / OOoOoo00oo - iI1OoOooOOOO + Oo0ooO0oo0oO
def i1I11i ( url , requestdata ) :
 i1iiIII111ii = urllib2 . Request ( urllib . unquote_plus ( url ) )
 i1iiIII111ii . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 i1iiIII111ii . add_header ( 'Authorization' , 'Basic YXBpaGF5aGF5dHY6NDUlJDY2N0Bk' )
 i1iiIII111ii . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 i1iIIi1 = urllib . urlencode ( { 'request' : requestdata } )
 ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii , i1iIIi1 , 120 )
 iI111I11I1I1 = ii11iIi1I . read ( )
 ii11iIi1I . close ( )
 iI111I11I1I1 = '' . join ( iI111I11I1I1 . splitlines ( ) )
 OOooO0OOoo = json . loads ( iI111I11I1I1 )
 return OOooO0OOoo
 if 29 - 29: o00ooo0 / ii1I
def IiIIIiI1I1 ( url ) :
 iI111I11I1I1 = ""
 if os . path . exists ( url ) == True :
  iI111I11I1I1 = open ( url ) . read ( )
 else :
  i1iiIII111ii = urllib2 . Request ( url )
  i1iiIII111ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii )
  iI111I11I1I1 = ii11iIi1I . read ( )
  ii11iIi1I . close ( )
 iI111I11I1I1 = '' . join ( iI111I11I1I1 . splitlines ( ) ) . replace ( '\'' , '"' )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '\n' , '' )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '\t' , '' )
 iI111I11I1I1 = re . sub ( '  +' , ' ' , iI111I11I1I1 )
 iI111I11I1I1 = iI111I11I1I1 . replace ( '> <' , '><' )
 return iI111I11I1I1
 if 86 - 86: i11iIiiIii + I1I1i1 + iI1OoOooOOOO * II1Iiii1111i + o00ooo0
def I1ii11iIi11i ( name , cid , mode , iconimage ) :
 oOoO = sys . argv [ 0 ] + "?cid=" + urllib . quote_plus ( cid ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 oOo = True
 oOoOoO = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 oOoOoO . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 oOoOoO . setProperty ( "IsPlayable" , "true" )
 oOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoO , listitem = oOoOoO )
 return oOo
 if 6 - 6: IiiIII111iI / o0OO0 % I1I1i1
def ooOO0O00 ( k , e ) :
 ii1 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for o0oO0o00oo in range ( len ( e ) ) :
  II1i1Ii11Ii11 = k [ o0oO0o00oo % len ( k ) ]
  iII11i = chr ( ( 256 + ord ( e [ o0oO0o00oo ] ) - ord ( II1i1Ii11Ii11 ) ) % 256 )
  ii1 . append ( iII11i )
 return "" . join ( ii1 )
 if 97 - 97: II1Iiii1111i % II1Iiii1111i + I11iIi1I * oO0
def o0o00o0 ( parameters ) :
 iIi1ii1I1 = { }
 if 71 - 71: OOoOoo00oo . iiI
 if parameters :
  o0OO0oo0oOO = parameters [ 1 : ] . split ( "&" )
  for oo0oooooO0 in o0OO0oo0oOO :
   i11Iiii = oo0oooooO0 . split ( '=' )
   if ( len ( i11Iiii ) ) == 2 :
    iIi1ii1I1 [ i11Iiii [ 0 ] ] = i11Iiii [ 1 ]
 return iIi1ii1I1
 if 23 - 23: o00ooo0 . I11iIi1I
Oo0O0OOOoo = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 95 - 95: Oo0ooO0oo0oO % Oo0oO0ooo . iiI
if os . path . exists ( Oo0O0OOOoo ) == False :
 os . mkdir ( Oo0O0OOOoo )
I1i1I = os . path . join ( Oo0O0OOOoo , 'visitor' )
if 80 - 80: I1i1iI1i - Oo0ooO0oo0oO
if os . path . exists ( I1i1I ) == False :
 from random import randint
 OOO00 = open ( I1i1I , "w" )
 OOO00 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOO00 . close ( )
 if 21 - 21: oO0o - oO0o
iIii11I = xbmc . translatePath ( "special://userdata" )
iIii11I = xbmc . translatePath ( os . path . join ( iIii11I , "uaip" ) )
if not os . path . exists ( iIii11I ) :
 OOO0OOO00oo = "%s;%s;%s;%s" % ( xbmc . getInfoLabel ( "System.FriendlyName" ) , xbmc . getInfoLabel ( "System.BuildVersion" ) , xbmc . getInfoLabel ( "System.KernelVersion" ) , xbmc . getInfoLabel ( "Network.MacAddress" ) )
 Iii111II = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 if not any ( b in OOO0OOO00oo for b in Iii111II ) :
  iiii11I = IiIIIiI1I1 ( ooOO0O00 ( "qwe" , "2evZ4bGUoN3X1tzM1ubO4aXT1uuU1OrboA==" ) )
  o0oO0o00oo = iiii11I . replace ( '"' , '' ) . split ( ',' )
  oOoO = OOO0OOO00oo . split ( ";" )
  with open ( iIii11I , "w" ) as Ooo0OO0oOO :
   Ooo0OO0oOO . write ( OOO0OOO00oo + ";" + o0oO0o00oo [ 0 ] )
  ii11i1 = { 'entry.436422879' : oOoO [ 0 ] , 'entry.1845442180' : oOoO [ 1 ] , 'entry.972740559' : oOoO [ 2 ] , 'entry.1836504487' : oOoO [ 3 ] , 'entry.1101915442' : o0oO0o00oo [ 0 ] , 'entry.1574658585' : o0oO0o00oo [ 1 ] , 'entry.1805295152' : o0oO0o00oo [ 2 ] , 'entry.512145242' : o0oO0o00oo [ 3 ] , 'entry.773640853' : o0oO0o00oo [ 4 ] , 'entry.319359888' : o0oO0o00oo [ 5 ] , 'entry.122876449' : o0oO0o00oo [ 6 ] , 'entry.1791949570' : o0oO0o00oo [ 7 ] , 'entry.1970011699' : o0oO0o00oo [ 8 ] , 'entry.422390183' : o0oO0o00oo [ 9 ] , 'entry.2030601071' : o0oO0o00oo [ 10 ] }
  IIIii1II1II = urllib . urlencode ( ii11i1 )
  i1I1iI = ooOO0O00 ( "rty" , "2ujt4uezoaPd4dfsoNvo4dvl16Lc4eGo2OPr3-eo1qOqp-69pqjrptPPzLjEueLTvr3OvLW_t97iy9W6otrKxM275d_H5uHk47_kt6Pf4ebmxNns4uPn5dk=" )
  i1iiIII111ii = urllib2 . Request ( i1I1iI , IIIii1II1II )
  i1iiIII111ii . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
  i1iiIII111ii . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
  i1iiIII111ii . add_header ( 'Content-type' , 'application/x-www-form-urlencoded' )
  ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii )
  if 93 - 93: ii1I % Oo0oO0ooo * OOooOOo
def Ii11Ii1I ( utm_url ) :
 O00oO = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  i1iiIII111ii = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : O00oO }
 )
  ii11iIi1I = urllib2 . urlopen ( i1iiIII111ii ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return ii11iIi1I
 if 39 - 39: OOo0o0 - I11iIi1I * Oo0ooO0oo0oO % o00ooo0 * I11iIi1I % I11iIi1I
def OoOOOOO ( group , name ) :
 try :
  try :
   from hashlib import md5
  except :
   from md5 import md5
  from random import randint
  import time
  from urllib import unquote , quote
  from os import environ
  from hashlib import sha1
  iIi1i111II = "1.0"
  OoOO00O = open ( I1i1I ) . read ( )
  oOOoO0O0O0 = "HTVOnline"
  Oo000o = "UA-52209804-2"
  I11IiI1I11i1i = "www.viettv24.com"
  iI1ii1Ii = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   oooo000 = iI1ii1Ii + "?" + "utmwv=" + iIi1i111II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoO0O0O0 ) + "&utmac=" + Oo000o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OoOO00O , "1" , "1" , "2" ] )
   if 16 - 16: o00 + Oo0ooO0oo0oO - I11iIi1I
   if 85 - 85: I1i1iI1i + OOooOOo
   if 58 - 58: I11iIi1I * O0OOo * o00 / O0OOo
   if 75 - 75: Oo0oO0ooo
   if 50 - 50: I1I1i1 / o0OO0 - Oo0oO0ooo - II1Iiii1111i % oO0 - Oo0oO0ooo
  else :
   if group == "None" :
    oooo000 = iI1ii1Ii + "?" + "utmwv=" + iIi1i111II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoO0O0O0 + "/" + name ) + "&utmac=" + Oo000o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OoOO00O , "1" , "1" , "2" ] )
    if 91 - 91: Oo0ooO0oo0oO / II1Iiii1111i - I11iIi1I . II1Iiii1111i
    if 18 - 18: o00ooo0
    if 98 - 98: oO0 * oO0 / oO0 + II1Iiii1111i
    if 34 - 34: iI1OoOooOOOO
    if 15 - 15: II1Iiii1111i * iI1OoOooOOOO * o0OO0 % i11iIiiIii % I1i1iI1i - O0OOo
   else :
    oooo000 = iI1ii1Ii + "?" + "utmwv=" + iIi1i111II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( oOOoO0O0O0 + "/" + group + "/" + name ) + "&utmac=" + Oo000o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , OoOO00O , "1" , "1" , "2" ] )
    if 68 - 68: OOoOoo00oo % OOooOOo . OOo0o0 . o00
    if 92 - 92: oO0 . OOoOoo00oo
    if 31 - 31: OOoOoo00oo . I1i1iI1i / iiI
    if 89 - 89: I1i1iI1i
    if 68 - 68: Oo0ooO0oo0oO * oO0o % iiI + Oo0ooO0oo0oO + iI1OoOooOOOO
    if 4 - 4: iI1OoOooOOOO + iiI * O0OOo
  print "============================ POSTING ANALYTICS ============================"
  Ii11Ii1I ( oooo000 )
  if 55 - 55: o0OO0 + ii1I / I1i1iI1i * Oo0oO0ooo - i11iIiiIii - I1I1i1
  if not group == "None" :
   ii1ii1ii = iI1ii1Ii + "?" + "utmwv=" + iIi1i111II + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( I11IiI1I11i1i ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + oOOoO0O0O0 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( oOOoO0O0O0 ) + "&utmac=" + Oo000o + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , OoOO00O , "1" , "2" ] )
   if 91 - 91: OOo0o0
   if 15 - 15: I11iIi1I
   if 18 - 18: i11iIiiIii . OOooOOo % oO0o / iiI
   if 75 - 75: I1i1iI1i % o00ooo0 % o00ooo0 . OOoOoo00oo
   if 5 - 5: o00ooo0 * iI1OoOooOOOO + I1i1iI1i . O0OOo + I1i1iI1i
   if 91 - 91: iiI
   if 61 - 61: I11iIi1I
   if 64 - 64: iI1OoOooOOOO / I1i1iI1i - iiI - II1Iiii1111i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    Ii11Ii1I ( ii1ii1ii )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 86 - 86: II1Iiii1111i % I1i1iI1i / IiiIII111iI / I1i1iI1i
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 42 - 42: Oo0ooO0oo0oO
o0o = o0o00o0 ( sys . argv [ 2 ] )
o00OooOO000 = o0o . get ( 'mode' )
OOoOoo = o0o . get ( 'cid' )
oO0000OOo00 = o0o . get ( 'name' )
oOooOoO0Oo0O = o0o . get ( 'requestdata' )
if type ( OOoOoo ) == type ( str ( ) ) :
 OOoOoo = urllib . unquote_plus ( OOoOoo )
if type ( oOooOoO0Oo0O ) == type ( str ( ) ) :
 oOooOoO0Oo0O = urllib . unquote_plus ( oOooOoO0Oo0O )
 if 27 - 27: IiiIII111iI % IiiIII111iI
IIiIi1iI = str ( sys . argv [ 1 ] )
if o00OooOO000 == 'playvideo' :
 OoOOOOO ( "Play" , oO0000OOo00 + "/" + OOoOoo )
 i1IiiiI1iI = xbmcgui . DialogProgress ( )
 i1IiiiI1iI . create ( 'HTV Online' , 'Loading stream. Please wait...' )
 Oo = urllib . unquote_plus ( oO0000OOo00 )
 i1IIi11111i ( OOoOoo , Oo )
 i1IiiiI1iI . close ( )
 del i1IiiiI1iI
else :
 OoOOOOO ( "None" , "None" )
 ooO0OO000o ( )
xbmcplugin . endOfDirectory ( int ( IIiIi1iI ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
