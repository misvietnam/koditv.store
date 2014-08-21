#!/usr/bin/python
# coding=utf8
import xbmc , xbmcaddon , xbmcplugin , xbmcgui , sys , urllib , urllib2 , re , os , zlib , base64
if 64 - 64: i11iIiiIii
OO0o = 'plugin.video.zingtv'
Oo0Ooo = xbmcaddon . Addon ( OO0o )
O0O0OO0O0O0 = int ( sys . argv [ 1 ] )
iiiii = ""
if 64 - 64: iIIi1iI1II111 + ii11i / oOooOoO0Oo0O
def iI1 ( ) :
 i1I11i ( 'Tìm kiếm' , '' , 'search' , 'http://echipstore.net/addonicons/Search.jpg' )
 i1I11i ( 'Thiếu nhi' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9ZIW8&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'TV Show' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0CE&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Phim Truyền Hình' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DW&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Hài kịch' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0D6&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Âm nhạc' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DC&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Video Games' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9ZIU8&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Hoạt hình' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DO&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Giáo dục' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0D7&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Thể thao' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0DI&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 i1I11i ( 'Tin tức - Sự kiện' , 'http://m.tv.zing.vn/ajax?f=genreProgram&s=new&id=IWZ9Z0CF&page=1&count=50' , 'indexprogram' , 'http://static.mp3.zdn.vn/skins/tv/images/zingtv-logo.png' )
 if 73 - 73: III - oo00oOOo * Oooo000o % OOo . OOO
 IiI1ii1 = xbmc . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'path' ) ) . decode ( "utf-8" )
 ##IiI1ii1 = xbmc . translatePath ( os . path . join ( IiI1ii1 , "temp.jpg" ) )
 ##urllib . urlretrieve ( 'http://echipstore.net/images/zingtv.jpg' , IiI1ii1 )
 ##oooOOooo = xbmcgui . ControlImage ( 0 , 0 , 1280 , 720 , IiI1ii1 )
 ##o0oo0oo0OO00 = xbmcgui . WindowDialog ( )
 ##o0oo0oo0OO00 . addControl ( oooOOooo )
 ##o0oo0oo0OO00 . doModal ( )
 if 20 - 20: i111iII
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 25 - 25: O0 + OoOoOoO0o0OO * Ooo0OO0oOO * Ii * o0o - OOO0o0o
def Ii1iI ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 Ooo = re . compile ( '<a class="content-items" href="(.+?)"><span class="video-img"><img alt="(.+?)" src="(.+?)" [^>]*>(.+?)<h4>(.+?)</h4>' ) . findall ( Oo )
 for o0oOoO00o , i1 , oOOoo00O0O , i1111 , i11 in reversed ( Ooo ) :
  I11 ( "[" + i11 + "] - " + i1 , "http://tv.zing.vn" + o0oOoO00o , 'loadvideo' , oOOoo00O0O )
 if ( len ( Ooo ) == 50 ) :
  Oo0o0000o0o0 = int ( re . compile ( '&page=(.+?)&' ) . findall ( url ) [ 0 ] )
  url = url . replace ( "&page=" + str ( Oo0o0000o0o0 ) , "&page=" + str ( Oo0o0000o0o0 + 1 ) )
  i1I11i ( "Next >>" , url , 'indexvideo' , "" )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 86 - 86: iiiii11iII1 % O0o
def oO0 ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 Ooo = re . compile ( '<a class="content-items" href="(.+?)"><img class="program-img" alt="(.+?)" src="(.+?)" [^>]*>' ) . findall ( Oo )
 for o0oOoO00o , i1 , oOOoo00O0O in Ooo :
  i1I11i ( "[B]" + i1 + "[/B]" , "http://m.tv.zing.vn" + o0oOoO00o , 'indexseries' , oOOoo00O0O )
 if ( len ( Ooo ) == 50 ) :
  Oo0o0000o0o0 = int ( re . compile ( '&page=(.+?)&' ) . findall ( url ) [ 0 ] )
  url = url . replace ( "&page=" + str ( Oo0o0000o0o0 ) , "&page=" + str ( Oo0o0000o0o0 + 1 ) )
  i1I11i ( "Next >>" , url , 'indexprogram' , "" )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(52)' )
  if 32 - 32: I1i1I - OoOoo0 % Oooo000o % Oooo000o
def iiI11 ( url ) :
 Oo = I1Ii11I1Ii1i ( url )
 OOooO = re . compile ( '<h3>(.+?)</h3>' ) . findall ( Oo ) [ 0 ]
 OOoO00o = re . compile ( '<input type="hidden" id="_objectId" objectType="tv_program" value="(.+?)">' ) . findall ( Oo ) [ 0 ]
 II111iiii = "http://m.tv.zing.vn/ajax?f=loadSuggest&type=tv_program&id=&page=1&count=100"
 II = I1Ii11I1Ii1i ( II111iiii . replace ( "id=" , "id=" + OOoO00o ) )
 Ooo = re . compile ( '<a href="(.+?)" [^>]*><img [^>]* src="(.+?)" alt="(.+?)">(.+?)<span>(.+?)</span></a>' ) . findall ( II )
 if 63 - 63: i111iII % III
 for o0oOoO00o , oOOoo00O0O , i1 , o0oOo0Ooo0O , OO00O0O0O00Oo in Ooo :
  OOoO00o = o0oOoO00o . split ( "/" ) [ - 1 ] . split ( "." ) [ 0 ]
  o0oOoO00o = "http://m.tv.zing.vn/ajax?f=loadMediaSeries&id=&page=1&count=50"
  i1I11i ( "[B]" + i1 + "[/B] (" + OO00O0O0O00Oo + ")" , o0oOoO00o . replace ( "id=" , "id=" + OOoO00o ) , 'indexvideo' , oOOoo00O0O )
 oOOo = xbmc . getSkinDir ( )
 if oOOo == 'skin.xeebo' :
  xbmc . executebuiltin ( 'Container.SetViewMode(50)' )
  if 25 - 25: O0 % oo00oOOo - oo00oOOo . oo00oOOo
def Ii1 ( ) :
 try :
  oOOoO0 = xbmc . Keyboard ( '' , 'Enter search text' )
  oOOoO0 . doModal ( )
  if ( oOOoO0 . isConfirmed ( ) ) :
   O0OoO000O0OO = urllib . quote_plus ( oOOoO0 . getText ( ) )
  iiI1IiI = 'http://m.tv.zing.vn/ajax?f=searchProgram&s=date&page=1&count=50&q=' + O0OoO000O0OO + '/'
  oO0 ( iiI1IiI )
 except : pass
 if 13 - 13: OOo . i11iIiiIii - ii11i - i111iII
def ii1I ( url , name ) :
 name = urllib . unquote_plus ( name ) . decode ( "utf-8" )
 Oo = I1Ii11I1Ii1i ( url )
 OooO0 = re . compile ( II11iiii1Ii ( "o" , 'q9jd3-Tjj-Po39SskdfY09PU3ZGP2NOskdzU09jQuNORj-XQ2-TUrJGXnZqumJGPnq0=' ) ) . findall ( Oo ) [ 0 ]
 Oo = I1Ii11I1Ii1i ( II11iiii1Ii ( "a" , "ydXV0ZuQkMLRyo_V14_bys_Ij9fPkJOPkZDOxsXKwpDKz8fQoM7GxcrCwMrFnofC0crAzMbanpqalpbDkpmSl8eSksfFmZWZxcOVl8SXkcLFxMXHmZeX" ) . replace ( "=&" , "=" + OooO0 + "&" ) )
 OO0oOoo = re . compile ( II11iiii1Ii ( "i" , 'i7_Szc7YoJuZi6OJi5GXlKiSiw==' ) ) . findall ( Oo )
 O0o0Oo = ""
 if len ( OO0oOoo ) == 0 :
  OO0oOoo = re . compile ( II11iiii1Ii ( "v" , 'mMzf2tvlqq6mmLCWmJ6kobWfmA==' ) ) . findall ( Oo )
  if len ( OO0oOoo ) == 0 :
   OO0oOoo = re . compile ( II11iiii1Ii ( "f" , 'iMzP0svF29jSiKCGiI6UkaWPiA==' ) ) . findall ( Oo )
  O0o0Oo = "http://" + OO0oOoo [ 0 ] . split ( "?" ) [ 0 ]
 else :
  O0o0Oo = "http://" + OO0oOoo [ 0 ] . split ( "?" ) [ 0 ]
  if 78 - 78: ii11i - OOO0o0o * OOO + O0 + iiiii11iII1 + iiiii11iII1
 I11I11i1I = xbmcgui . ListItem ( name )
 I11I11i1I . setInfo ( 'video' , { 'Title' : name } )
 I11I11i1I . setProperty ( "IsPlayable" , "true" )
 I11I11i1I . setPath ( O0o0Oo )
 xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , I11I11i1I )
 if 49 - 49: oo00oOOo % iiiii11iII1 * iIIi1iI1II111
def I1Ii11I1Ii1i ( url ) :
 oOOo0oo = urllib2 . Request ( url )
 oOOo0oo . add_header ( 'User-Agent' , 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)' )
 oOOo0oo . add_header ( 'Accept' , 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' )
 o0oo0o0O00OO = urllib2 . urlopen ( oOOo0oo )
 Oo = o0oo0o0O00OO . read ( )
 o0oo0o0O00OO . close ( )
 Oo = '' . join ( Oo . splitlines ( ) ) . replace ( '\'' , '"' )
 Oo = Oo . replace ( '\n' , '' )
 Oo = Oo . replace ( '\t' , '' )
 Oo = re . sub ( '  +' , ' ' , Oo )
 Oo = Oo . replace ( '> <' , '><' )
 return Oo
 if 80 - 80: III
def II11iiii1Ii ( k , e ) :
 oOOO0o0o = [ ]
 e = base64 . urlsafe_b64decode ( e )
 for iiI1 in range ( len ( e ) ) :
  i11Iiii = k [ iiI1 % len ( k ) ]
  iI = chr ( ( 256 + ord ( e [ iiI1 ] ) - ord ( i11Iiii ) ) % 256 )
  oOOO0o0o . append ( iI )
 return "" . join ( oOOO0o0o )
 if 28 - 28: Ii - O0o . O0o + i111iII - oOooOoO0Oo0O + iIIi1iI1II111
def I11 ( name , url , mode , iconimage ) :
 oOoOooOo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOOO = True
 OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultVideo.png" , thumbnailImage = iconimage )
 OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOO00 . setProperty ( "IsPlayable" , "true" )
 OOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOooOo0o0 , listitem = OOO00 )
 return OOOO
 if 21 - 21: oOooOoO0Oo0O - oOooOoO0Oo0O
def i1I11i ( name , url , mode , iconimage ) :
 oOoOooOo0o0 = sys . argv [ 0 ] + "?url=" + urllib . quote_plus ( url ) + "&mode=" + str ( mode ) + "&name=" + urllib . quote_plus ( name )
 OOOO = True
 OOO00 = xbmcgui . ListItem ( name , iconImage = "DefaultFolder.png" , thumbnailImage = iconimage )
 OOO00 . setInfo ( type = "Video" , infoLabels = { "Title" : name } )
 OOOO = xbmcplugin . addDirectoryItem ( handle = int ( sys . argv [ 1 ] ) , url = oOoOooOo0o0 , listitem = OOO00 , isFolder = True )
 return OOOO
 if 8 - 8: i111iII
def o00O ( parameters ) :
 OOO0OOO00oo = { }
 if 31 - 31: oo00oOOo - Ii . I1i1I % i111iII - iIIi1iI1II111
 if parameters :
  iii11 = parameters [ 1 : ] . split ( "&" )
  for O0oo0OO0oOOOo in iii11 :
   i1i1i11IIi = O0oo0OO0oOOOo . split ( '=' )
   if ( len ( i1i1i11IIi ) ) == 2 :
    OOO0OOO00oo [ i1i1i11IIi [ 0 ] ] = i1i1i11IIi [ 1 ]
 return OOO0OOO00oo
 if 33 - 33: O0 + Ii * OOO - OOo / Ooo0OO0oOO % OOO0o0o
II1i1IiiIIi11 = o00O ( sys . argv [ 2 ] )
iI1Ii11iII1 = II1i1IiiIIi11 . get ( 'mode' )
iiI1IiI = II1i1IiiIIi11 . get ( 'url' )
Oo0O0O0ooO0O = II1i1IiiIIi11 . get ( 'name' )
if type ( iiI1IiI ) == type ( str ( ) ) :
 iiI1IiI = urllib . unquote_plus ( iiI1IiI )
 if 15 - 15: OoOoOoO0o0OO + i111iII - oOooOoO0Oo0O / Ii
oo000OO00Oo = str ( sys . argv [ 1 ] )
if iI1Ii11iII1 == 'indexvideo' :
 Ii1iI ( iiI1IiI )
elif iI1Ii11iII1 == 'indexprogram' :
 oO0 ( iiI1IiI )
elif iI1Ii11iII1 == 'indexseries' :
 iiI11 ( iiI1IiI )
elif iI1Ii11iII1 == 'search' :
 Ii1 ( )
elif iI1Ii11iII1 == 'loadvideo' :
 O0OOO0OOoO0O = xbmcgui . DialogProgress ( )
 O0OOO0OOoO0O . create ( 'Zing TV' , 'Loading video. Please wait...' )
 ii1I ( iiI1IiI , Oo0O0O0ooO0O )
 O0OOO0OOoO0O . close ( )
 del O0OOO0OOoO0O
else :
 iI1 ( )
xbmcplugin . endOfDirectory ( int ( oo000OO00Oo ) ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
