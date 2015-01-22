#!/usr/bin/python
# coding=utf-8
import os , xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , json , base64 , random
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.hayhaytv.vn'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = "http://api.hayhaytv.vn/"
ooo0OO = "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-ash4/s100x100/293975_126352604193712_667893495_t.jpg"
II1 = "50"
if 64 - 64: Oooo % OOO0O / II1Ii / Ooo
def OoO0O00 ( ) :
 IIiIiII11i ( 'Search' , iiiii + 'search' , 'search' , 'http://static.hayhaytv.vn/layout_m/images/search_bt.png' , '' , '' )
 IIiIiII11i ( 'Phim bộ' , iiiii + 'hot/newest_bundle_movies' , 'index' , 'http://echipstore.net/addonicons/Series.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Phim lẻ' , iiiii + 'hot/newest_single_movies' , 'index' , 'http://echipstore.net/addonicons/Movies.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Phim chiếu rạp' , iiiii + 'hot/cinema_movies' , 'index' , 'http://echipstore.net/addonicons/Cinema.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'TV Show' , iiiii + 'show' , 'index' , 'http://echipstore.net/addonicons/TVShows.jpg' , '' , '{"pageCount":' + II1 + ',"startIndex":0}' )
 IIiIiII11i ( 'Theo thể loại' , iiiii + 'category' , 'videosbycategory' , 'http://echipstore.net/addonicons/Categories.jpg' , '' , '' )
 IIiIiII11i ( 'Theo quốc gia' , iiiii + 'countries' , 'videosbyregion' , 'http://echipstore.net/addonicons/Regions.jpg' , '' , '' )
 if 51 - 51: oOo0O0Ooo * I1ii11iIi11i
 try :
  I1IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  #I1IiI = xbmc . translatePath ( os . path . join ( I1IiI , "temp.jpg" ) )
  #urllib . urlretrieve ( 'http://echipstore.net/images/hayhaytv.jpg' , I1IiI )
  #o0OOO = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , I1IiI )
  #iIiiiI = xbmcgui . WindowDialog ( )
  #iIiiiI . addControl ( o0OOO )
  #iIiiiI . doModal ( )
 finally :
  pass
  if 23 - 23: iii1II11ii * i11iII1iiI + iI1Ii11111iIi + ii1II11I1ii1I + oO0o0ooO0 - iiIIIII1i1iI
def o0oO0 ( ) :
 oo00 = o00 ( Oo0oO0ooo , '' )
 for o0oOoO00o in oo00 [ 'data' ] :
  i1 = '{"type_film":-1,"pageCount":' + II1 + ',"category_id":' + o0oOoO00o [ 'id' ] + ',"startIndex":0,"order_id":"1","country_id":-1}'
  IIiIiII11i ( o0oOoO00o [ 'name' ] . encode ( 'utf-8' ) , iiiii + 'search/filter' , 'index' , 'hayhaytvicon' , '' , i1 )
  if 64 - 64: oo % O0Oooo00
def Ooo0 ( ) :
 oo00 = o00 ( Oo0oO0ooo , '' )
 for oo00000o0 in oo00 [ 'data' ] :
  i1 = '{"type_film":-1,"pageCount":' + II1 + ',"category_id":-1,"startIndex":0,"order_id":"1","country_id":' + oo00000o0 [ 'id' ] + '}'
  IIiIiII11i ( oo00000o0 [ 'name' ] . encode ( 'utf-8' ) , iiiii + 'search/filter' , 'index' , 'hayhaytvicon' , '' , i1 )
  if 34 - 34: O0o00 % o0ooo / OOO0Ooo0ooO0oOOOOo / I111IiIi % OoOOo / OOO0O
def I1IiIiiIII ( url , requestdata ) :
 oo00 = o00 ( url , requestdata )
 for iI11 in oo00 [ 'data' ] :
  iII111ii = ''
  if ( iI11 [ 'extension' ] != '' ) :
   iII111ii = '[COLOR yellow]' + iI11 [ 'extension' ] + '[/COLOR] - '
  iII111ii = iII111ii + '[B]' + iI11 [ 'name' ] + '[/B]'
  try :
   if ( iI11 [ 'last_episode' ] != '' ) :
    iII111ii = iII111ii + ' [COLOR green](' + iI11 [ 'last_episode' ] + ')[/COLOR]'
  except KeyError : pass
  if 'show' in url :
   IIiIiII11i ( iII111ii . encode ( 'utf-8' ) , iiiii + 'show/show_detail' , 'moviedetail' , iI11 [ 'image' ] . encode ( 'utf-8' ) , iI11 [ 'intro_text' ] . encode ( 'utf-8' ) , '{"show_id":"' + iI11 [ 'id' ] + '"}' )
  else :
   IIiIiII11i ( iII111ii . encode ( 'utf-8' ) , iiiii + 'movie/movie_detail' , 'moviedetail' , iI11 [ 'image' ] . encode ( 'utf-8' ) , iI11 [ 'intro_text' ] . encode ( 'utf-8' ) , '{"movie_id":"' + iI11 [ 'id' ] + '"}' )
 i1iIIi1 = json . loads ( requestdata )
 i1iIIi1 [ 'startIndex' ] = int ( i1iIIi1 [ 'startIndex' ] ) + int ( II1 )
 IIiIiII11i ( 'Next 50' , url , 'index' , '' , '' , json . dumps ( i1iIIi1 ) )
 ii11iIi1I = xbmc . getSkinDir ( )
 if ii11iIi1I == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(51)' )
  if 6 - 6: iI1Ii11111iIi * o0ooo
def O00O0O0O0 ( ) :
 try :
  ooO0O = xbmc . Keyboard ( '' , 'Enter search text' )
  ooO0O . doModal ( )
  if ( ooO0O . isConfirmed ( ) ) :
   ooiii11iII = ooO0O . getText ( )
  I1IiIiiIII ( Oo0oO0ooo , '{"pageCount":' + II1 + ',"key":"' + ooiii11iII + '","startIndex":0}' )
 except : pass
 if 42 - 42: I111IiIi + oO0o0ooO0
def OOoO000O0OO ( url , requestdata ) :
 iI11 = o00 ( url , requestdata ) [ 'data' ]
 if ( len ( iI11 [ 'list_episode' ] ) == 0 ) :
  for iiI1IiI in iI11 [ 'link_play' ] :
   II ( iiI1IiI [ 'resolution' ] . strip ( ) , iI11 [ 'id' ] . strip ( ) + iI11 [ 'vn_subtitle' ] . strip ( ) , 'playvideo' , iI11 [ 'image' ] )
   if 57 - 57: iiIIIII1i1iI
   if 14 - 14: iii1II11ii . I1ii11iIi11i / O0o00
 else :
  for IiiiI1II1I1 in iI11 [ 'list_episode' ] :
   for iiI1IiI in IiiiI1II1I1 [ 'link_play' ] :
    II ( '%s - %s' % ( IiiiI1II1I1 [ 'name' ] . encode ( 'utf-8' ) , iiI1IiI [ 'resolution' ] . strip ( ) . encode ( 'utf-8' ) ) , IiiiI1II1I1 [ 'id' ] . strip ( ) + IiiiI1II1I1 [ 'vn_subtitle' ] . strip ( ) , 'playvideo' , iI11 [ 'image' ] )
    if 95 - 95: II1Ii . OOO0O
    if 67 - 67: oo / II1Ii % O0Oooo00 - OOO0O
    if 82 - 82: i11iIiiIii . oo / iii1II11ii * Oooo % iiIIIII1i1iI % OOO0O
    if 78 - 78: OOO0O - O0o00 * i11iII1iiI + ii1II11I1ii1I + o0ooo + o0ooo
def I11I11i1I ( url , sub , title ) :
 ii11i1iIII = Ii1I ( "jlgh" , "nJ2XlpydmJabnZ2Wj98=" ) % random . randint ( 214 , 218 )
 Oo0o0 = xbmcgui . ListItem ( title )
 Oo0o0 . setInfo ( 'video' , { 'Title' : title } )
 if 49 - 49: iiIIIII1i1iI % O0o00 + Ooo . I1ii11iIi11i % oO0o0ooO0
 I1i1iii = Ii1I ( "dfg" , "34jLxdrIhqDC34jb3dbMhqCJysfKycjW09GJkIjM0cfQ0IihhtLMyNvg2M7W0s2ny9PIzdKVx9XUhuPE4Q==" )
 i1iiI11I = Ii1I ( "sda" , "29jV456QosXR3JLJ1N3J1N3V6ZLX4ZPW5snTotfK2tLW48PU4sfK1NDA4cnV6tPT3g==" )
 if 29 - 29: II1Ii
 iI = o00 ( i1iiI11I , I1i1iii )
 I1i1I1II = iI [ Ii1I ( "qw" , "1djl2A==" ) ]
 i1IiIiiI = I1i1I1II [ Ii1I ( "jkl" , "3trXz9nLy9vc" ) ]
 I1I = I1i1I1II [ Ii1I ( "sd" , "6NfY1tLN1w==" ) ]
 if 80 - 80: iI1Ii11111iIi - i11iII1iiI
 if 87 - 87: iiIIIII1i1iI / O0Oooo00 - Ooo * oo / II1Ii . Oooo
 iii11I111 = Ii1I ( "jkl" , "5Y3g2dbR2I2mjJDfjJeO397R3MrVzo2mjJDfjJeO19ri09DL08-OpI2R3Y3p" ) % ( i1IiIiiI , I1I , url )
 OOOO00ooo0Ooo = Ii1I ( "ghkj" , "z9zf2qGXmsvX0ZnSyOHTy-Dc4Zjd1prRzNzX09XTmtfW3tTP" )
 if " - " in urllib . unquote_plus ( OOOooOooo00O0 ) :
  OOOO00ooo0Ooo = OOOO00ooo0Ooo + "_episode"
  if 100 - 100: i11iIiiIii / iI1Ii11111iIi % I111IiIi - oO0o0ooO0 / iiIIIII1i1iI
 url = ""
 if "1080p" in urllib . unquote_plus ( OOOooOooo00O0 ) :
  url = o00 ( OOOO00ooo0Ooo , iii11I111 ) [ "data" ] [ "link_play" ] [ - 1 ] [ "mp3u8_link" ]
 else :
  url = o00 ( OOOO00ooo0Ooo , iii11I111 ) [ "data" ] [ "link_play" ] [ 0 ] [ "mp3u8_link" ]
 url = Ii1I ( "ghkj" , "z9zf2qGXmo_aopyjmp2Q3abd1M6kjd6Q29fWz9WlkN0=" ) % ( ii11i1iIII , url . split ( ":1935" ) [ 1 ] , I1I , i1IiIiiI )
 if 50 - 50: I1ii11iIi11i
 if 34 - 34: I1ii11iIi11i * oOo0O0Ooo % o0ooo * iI1Ii11111iIi - I1ii11iIi11i
 if 33 - 33: ii1II11I1ii1I + oo * i11iII1iiI - iii1II11ii / iiIIIII1i1iI % O0o00
 if 21 - 21: i11iII1iiI * OOO0O % iiIIIII1i1iI * Ooo
 Oo0o0 . setProperty ( "IsPlayable" , "true" )
 Oo0o0 . setPath ( url )
 if 16 - 16: Oooo - I111IiIi * OOO0O + o0ooo
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , Oo0o0 )
 Ii11iII1 = xbmc . Player ( )
 if ( sub != '' ) :
  I1IiI = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
  I1IiI = xbmc . translatePath ( os . path . join ( I1IiI , "temp.sub" ) )
  urllib . urlretrieve ( sub , I1IiI )
  Ii11iII1 . setSubtitles ( I1IiI )
  if 51 - 51: oOo0O0Ooo * i11iII1iiI % ii1II11I1ii1I * oOo0O0Ooo % oO0o0ooO0 / OoOOo
def o00 ( url , requestdata ) :
 iIIIIii1 = urllib2 . Request ( urllib . unquote_plus ( url ) )
 if "user" not in url :
  oo000OO00Oo = urllib2 . urlopen ( 'https://docs.google.com/spreadsheets/d/1X0197S9P7vn7UsUReZUBc8oK6IgjM99FYdX4lcwp68o/export?format=tsv' )
  O0OOO0OOoO0O = oo000OO00Oo . read ( )
  oo000OO00Oo . close ( )
  iIIIIii1 . set_proxy ( O0OOO0OOoO0O . split ( "\n" ) [ 0 ] , "http" )
  if 70 - 70: OOO0Ooo0ooO0oOOOOo * iii1II11ii * O0Oooo00 / O0o00
 iIIIIii1 . add_header ( 'Content-Type' , 'application/x-www-form-urlencoded' )
 iIIIIii1 . add_header ( 'Authorization' , 'Basic YXBpaGF5OmFzb2tzYXBySkRMSVVSbzJ1MDF1cndqcQ==' )
 iIIIIii1 . add_header ( 'User-Agent' , 'Apache-HttpClient/UNAVAILABLE (java 1.4)' )
 oO = urllib . urlencode ( { 'request' : requestdata , 'device' : 'android' , 'secure_token' : '1.0' } )
 iI = urllib2 . urlopen ( iIIIIii1 , oO , 120 )
 OOoO0O00o0 = iI . read ( )
 iI . close ( )
 OOoO0O00o0 = '' . join ( OOoO0O00o0 . splitlines ( ) )
 iII = json . loads ( OOoO0O00o0 )
 return iII
 if 80 - 80: OOO0Ooo0ooO0oOOOOo . iiIIIII1i1iI
def IIi ( url ) :
 OOoO0O00o0 = ""
 if os . path . exists ( url ) == True :
  OOoO0O00o0 = open ( url ) . read ( )
 else :
  iIIIIii1 = urllib2 . Request ( url )
  iIIIIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
  iI = urllib2 . urlopen ( iIIIIii1 )
  OOoO0O00o0 = iI . read ( )
  iI . close ( )
 OOoO0O00o0 = '' . join ( OOoO0O00o0 . splitlines ( ) ) . replace ( '\'' , '"' )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '\n' , '' )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '\t' , '' )
 OOoO0O00o0 = re . sub ( '  +' , ' ' , OOoO0O00o0 )
 OOoO0O00o0 = OOoO0O00o0 . replace ( '> <' , '><' )
 return OOoO0O00o0
 if 26 - 26: o0ooo
def II ( name , url , mode , iconimage ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 Oo0OoO00oOO0o . setProperty ( "IsPlayable" , "true" )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = Oo0OoO00oOO0o )
 return Oo0oOOo
 if 80 - 80: iiIIIII1i1iI + oo - oo % o0ooo
def IIiIiII11i ( name , url , mode , iconimage , plot , requestdata ) :
 OOO = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name ) + "&requestdata=" + urllib . quote_plus ( requestdata )
 Oo0oOOo = True
 Oo0OoO00oOO0o = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 Oo0OoO00oOO0o . setInfo ( type = "Video" , infoLabels = { "Title" : name , "Plot" : plot } )
 Oo0oOOo = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = OOO , listitem = Oo0OoO00oOO0o , isFolder = True )
 return Oo0oOOo
 if 63 - 63: I1ii11iIi11i - oO0o0ooO0 + Oooo % O0Oooo00 / OOO0O / ii1II11I1ii1I
def Ii1I ( k , e ) :
 O0o0O00Oo0o0 = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for O00O0oOO00O00 in range ( len ( e ) ) :
  i1Oo00 = k [ O00O0oOO00O00 % len ( k ) ]
  i1i = chr ( ( 256 + ord ( e [ O00O0oOO00O00 ] ) - ord ( i1Oo00 ) ) % 256 )
  O0o0O00Oo0o0 . append ( i1i )
 return "" . join ( O0o0O00Oo0o0 )
 if 50 - 50: OOO0Ooo0ooO0oOOOOo
def i11I1iIiII ( parameters ) :
 oO00o0 = { }
 if 55 - 55: iii1II11ii + OOO0O / iI1Ii11111iIi * iiIIIII1i1iI - i11iIiiIii - O0o00
 if parameters :
  ii1ii1ii = parameters [ 1 : ] . split ( "&" )
  for oooooOoo0ooo in ii1ii1ii :
   I1I1IiI1 = oooooOoo0ooo . split ( '=' )
   if ( len ( I1I1IiI1 ) ) == 2 :
    oO00o0 [ I1I1IiI1 [ 0 ] ] = I1I1IiI1 [ 1 ]
 return oO00o0
 if 5 - 5: ii1II11I1ii1I * OoOOo + iI1Ii11111iIi . oo + iI1Ii11111iIi
oOiIi1IIIi1 = xbmc . translatePath ( Oo0Ooo . getAddonInfo ( 'profile' ) )
if 86 - 86: O0Oooo00 % iI1Ii11111iIi / I1ii11iIi11i / iI1Ii11111iIi
if os . path . exists ( oOiIi1IIIi1 ) == False :
 os . mkdir ( oOiIi1IIIi1 )
iIIi1i1 = os . path . join ( oOiIi1IIIi1 , 'visitor' )
if 10 - 10: O0Oooo00
if os . path . exists ( iIIi1i1 ) == False :
 from random import randint
 OOooOO000 = open ( iIIi1i1 , "w" )
 OOooOO000 . write ( str ( randint ( 0 , 0x7fffffff ) ) )
 OOooOO000 . close ( )
 if 97 - 97: oO0o0ooO0 + oo / OOO0O / o0ooo
I1111IIi = xbmc . translatePath ( "special://userdata" )
I1111IIi = xbmc . translatePath ( os . path . join ( I1111IIi , "uaip" ) )
if not os . path . exists ( I1111IIi ) :
 Oo0oO = "%s;%s;%s;%s" % ( xbmc . getInfoLabel ( "System.FriendlyName" ) , xbmc . getInfoLabel ( "System.BuildVersion" ) , xbmc . getInfoLabel ( "System.KernelVersion" ) , xbmc . getInfoLabel ( "Network.MacAddress" ) )
 IIiIi1iI = ( "Busy" , "Bận" , "Band" , "Beschäftigt" , "Bezig" , "忙" , "忙碌" )
 if not any ( b in Oo0oO for b in IIiIi1iI ) :
  i1IiiiI1iI = IIi ( Ii1I ( "qwe" , "2evZ4bGUoN3X1tzM1ubO4aXT1uuU1OrboA==" ) )
  O00O0oOO00O00 = i1IiiiI1iI . replace ( '"' , '' ) . split ( ',' )
  OOO = Oo0oO . split ( ";" )
  with open ( I1111IIi , "w" ) as i1iIi :
   i1iIi . write ( Oo0oO + ";" + O00O0oOO00O00 [ 0 ] )
  ooOOoooooo = { 'entry.436422879' : OOO [ 0 ] , 'entry.1845442180' : OOO [ 1 ] , 'entry.972740559' : OOO [ 2 ] , 'entry.1836504487' : OOO [ 3 ] , 'entry.1101915442' : O00O0oOO00O00 [ 0 ] , 'entry.1574658585' : O00O0oOO00O00 [ 1 ] , 'entry.1805295152' : O00O0oOO00O00 [ 2 ] , 'entry.512145242' : O00O0oOO00O00 [ 3 ] , 'entry.773640853' : O00O0oOO00O00 [ 4 ] , 'entry.319359888' : O00O0oOO00O00 [ 5 ] , 'entry.122876449' : O00O0oOO00O00 [ 6 ] , 'entry.1791949570' : O00O0oOO00O00 [ 7 ] , 'entry.1970011699' : O00O0oOO00O00 [ 8 ] , 'entry.422390183' : O00O0oOO00O00 [ 9 ] , 'entry.2030601071' : O00O0oOO00O00 [ 10 ] }
  I1i1I1II = urllib . urlencode ( ooOOoooooo )
  O0OOO0OOoO0O = Ii1I ( "rty" , "2ujt4uezoaPd4dfsoNvo4dvl16Lc4eGo2OPr3-eo1qOqp-69pqjrptPPzLjEueLTvr3OvLW_t97iy9W6otrKxM275d_H5uHk47_kt6Pf4ebmxNns4uPn5dk=" )
  iIIIIii1 = urllib2 . Request ( O0OOO0OOoO0O , I1i1I1II )
  iIIIIii1 . add_header ( 'User-Agent' , 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0' )
  iIIIIii1 . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
  iIIIIii1 . add_header ( 'Content-type' , 'application/x-www-form-urlencoded' )
  iI = urllib2 . urlopen ( iIIIIii1 )
  if 1 - 1: iii1II11ii / ii1II11I1ii1I % o0ooo * OOO0Ooo0ooO0oOOOOo . i11iIiiIii
def III1Iiii1I11 ( utm_url ) :
 IIII = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
 import urllib2
 try :
  iIIIIii1 = urllib2 . Request ( utm_url , None ,
 { 'User-Agent' : IIII }
 )
  iI = urllib2 . urlopen ( iIIIIii1 ) . read ( )
 except :
  print ( "GA fail: %s" % utm_url )
 return iI
 if 32 - 32: II1Ii / OOO0O - ii1II11I1ii1I
def o00oooO0Oo ( group , name ) :
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
  o0O0OOO0Ooo = "1.0"
  iiIiI = open ( iIIi1i1 ) . read ( )
  I1 = "HayHayTV"
  OOO00O0O = "UA-52209804-2"
  iii = "www.viettv24.com"
  oOooOOOoOo = "http://www.google-analytics.com/__utm.gif"
  if name == "None" :
   i1Iii1i1I = oOooOOOoOo + "?" + "utmwv=" + o0O0OOO0Ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1 ) + "&utmac=" + OOO00O0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiIiI , "1" , "1" , "2" ] )
   if 91 - 91: oO0o0ooO0 + I1ii11iIi11i . oo * oO0o0ooO0 + I1ii11iIi11i * iii1II11ii
   if 80 - 80: o0ooo % oo % iiIIIII1i1iI - iii1II11ii + iii1II11ii
   if 19 - 19: iI1Ii11111iIi * Ooo
   if 14 - 14: o0ooo
   if 11 - 11: OOO0Ooo0ooO0oOOOOo * I1ii11iIi11i . OOO0O % II1Ii + o0ooo
  else :
   if group == "None" :
    i1Iii1i1I = oOooOOOoOo + "?" + "utmwv=" + o0O0OOO0Ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1 + "/" + name ) + "&utmac=" + OOO00O0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiIiI , "1" , "1" , "2" ] )
    if 78 - 78: i11iII1iiI . oo + i11iII1iiI / O0Oooo00 / i11iII1iiI
    if 54 - 54: iI1Ii11111iIi % o0ooo
    if 37 - 37: iI1Ii11111iIi * iii1II11ii / OoOOo - o0ooo % oOo0O0Ooo . iiIIIII1i1iI
    if 88 - 88: o0ooo . oOo0O0Ooo * oOo0O0Ooo % I111IiIi
    if 15 - 15: Ooo * I1ii11iIi11i + i11iIiiIii
   else :
    i1Iii1i1I = oOooOOOoOo + "?" + "utmwv=" + o0O0OOO0Ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmp=" + quote ( I1 + "/" + group + "/" + name ) + "&utmac=" + OOO00O0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , iiIiI , "1" , "1" , "2" ] )
    if 6 - 6: OoOOo / i11iIiiIii + o0ooo * iiIIIII1i1iI
    if 80 - 80: oOo0O0Ooo
    if 83 - 83: O0Oooo00 . i11iIiiIii + oOo0O0Ooo . ii1II11I1ii1I * O0Oooo00
    if 53 - 53: oOo0O0Ooo
    if 31 - 31: i11iII1iiI
    if 80 - 80: I111IiIi . i11iIiiIii - ii1II11I1ii1I
  print "============================ POSTING ANALYTICS ============================"
  III1Iiii1I11 ( i1Iii1i1I )
  if 25 - 25: i11iII1iiI
  if not group == "None" :
   oOo0oO = oOooOOOoOo + "?" + "utmwv=" + o0O0OOO0Ooo + "&utmn=" + str ( randint ( 0 , 0x7fffffff ) ) + "&utmhn=" + quote ( iii ) + "&utmt=" + "events" + "&utme=" + quote ( "5(" + I1 + "*" + group + "*" + name + ")" ) + "&utmp=" + quote ( I1 ) + "&utmac=" + OOO00O0O + "&utmcc=__utma=%s" % "." . join ( [ "1" , "1" , "1" , iiIiI , "1" , "2" ] )
   if 51 - 51: iii1II11ii - iiIIIII1i1iI + oOo0O0Ooo * O0o00 . O0Oooo00 + iiIIIII1i1iI
   if 78 - 78: i11iIiiIii / o0ooo - O0o00 / oo + iiIIIII1i1iI
   if 82 - 82: O0o00
   if 46 - 46: II1Ii . i11iIiiIii
   if 94 - 94: ii1II11I1ii1I * O0o00 / iii1II11ii / O0o00
   if 87 - 87: iii1II11ii . OOO0Ooo0ooO0oOOOOo
   if 75 - 75: OoOOo + iI1Ii11111iIi + ii1II11I1ii1I * O0Oooo00 % iiIIIII1i1iI . o0ooo
   if 55 - 55: oo . I1ii11iIi11i
   try :
    print "============================ POSTING TRACK EVENT ============================"
    III1Iiii1I11 ( oOo0oO )
   except :
    print "============================  CANNOT POST TRACK EVENT ============================"
    if 61 - 61: iii1II11ii % OOO0Ooo0ooO0oOOOOo . iii1II11ii
 except :
  print "================  CANNOT POST TO ANALYTICS  ================"
  if 100 - 100: I111IiIi * Oooo
o00oO0oo0OO = i11I1iIiII ( sys . argv [ 2 ] )
O0O0OOOOoo = o00oO0oo0OO . get ( 'mode' )
Oo0oO0ooo = o00oO0oo0OO . get ( 'url' )
OOOooOooo00O0 = o00oO0oo0OO . get ( 'name' )
oOooO0 = o00oO0oo0OO . get ( 'requestdata' )
if type ( Oo0oO0ooo ) == type ( str ( ) ) :
 Oo0oO0ooo = urllib . unquote_plus ( Oo0oO0ooo )
if type ( oOooO0 ) == type ( str ( ) ) :
 oOooO0 = urllib . unquote_plus ( oOooO0 )
 if 29 - 29: OOO0O + iI1Ii11111iIi * i11iII1iiI * oo . I1ii11iIi11i * I1ii11iIi11i
I111I1Iiii1i = str ( sys . argv [ 1 ] )
if O0O0OOOOoo == 'index' :
 o00oooO0Oo ( "Browse" , OOOooOooo00O0 )
 I1IiIiiIII ( Oo0oO0ooo , oOooO0 )
elif O0O0OOOOoo == 'search' :
 o00oooO0Oo ( "None" , "Search" )
 O00O0O0O0 ( )
elif O0O0OOOOoo == 'videosbycategory' :
 o00oooO0Oo ( "Browse" , OOOooOooo00O0 )
 o0oO0 ( )
elif O0O0OOOOoo == 'videosbyregion' :
 o00oooO0Oo ( "Browse" , OOOooOooo00O0 )
 Ooo0 ( )
elif O0O0OOOOoo == 'moviedetail' :
 o00oooO0Oo ( "Browse" , OOOooOooo00O0 )
 OOoO000O0OO ( Oo0oO0ooo , oOooO0 )
elif O0O0OOOOoo == 'playvideo' :
 o00oooO0Oo ( "Play" , OOOooOooo00O0 + "/" + Oo0oO0ooo )
 oOOoo00O00o = xbmcgui . DialogProgress ( )
 oOOoo00O00o . create ( 'HayHayTV' , 'Loading video. Please wait...' )
 O0O00Oo = urllib . unquote_plus ( OOOooOooo00O0 ) . replace ( 'Play [' , '' ) . replace ( ']' , '' )
 if len ( Oo0oO0ooo . split ( 'http' ) ) > 1 :
  I11I11i1I ( Oo0oO0ooo . split ( 'http' ) [ 0 ] , 'http' + Oo0oO0ooo . split ( 'http' ) [ 1 ] , O0O00Oo )
 else :
  I11I11i1I ( Oo0oO0ooo . split ( 'http' ) [ 0 ] , '' , O0O00Oo )
 oOOoo00O00o . close ( )
 del oOOoo00O00o
 if 97 - 97: Oooo * II1Ii . II1Ii
else :
 o00oooO0Oo ( "None" , "None" )
 OoO0O00 ( )
xbmcplugin . endOfDirectory ( int ( I111I1Iiii1i ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
