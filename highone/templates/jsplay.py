# coding=utf8
import os
import sys
import PyV8

reload(sys)
sys.setdefaultencoding('utf8')

# js = """function mee(){
# 		var sDesc = '11.DOC,22.DOC,33.DOC';
# 		var sUrl = './P020110715543179340497.doc,./P020110715543179604988.doc,./P020110715543179915322.doc';
# 					var aDesc = sDesc.split(",");
# 					var aUrl = sUrl.split(",");
# 					for (var i = 0; i < aDesc.length; i++){
# 	                                    return ("<a  href='" + aUrl[i] + "'>" + aDesc[i] + "</a>");
# 		}
# 		}"""

js = r'var eg="/registerValidate.jspx?t=149",fg="uhq",ch,ah=new Array(),bh;function cg(dg){for(ch=0;ch<bh.length;ch++)ah[ch]=bh.charCodeAt(ch);ch="for(ch=49;;){if(ch<3)break;ah[ch]=(ah[ch]-ah[ch-1])&0xff;ch--;}";eval(ch);ch=3;for(;;){if(ch>48)break;ah[ch]=(((((ah[ch]-ah[ch+1])&0xff)-92)&0xff)-37)&0xff;ch++;}ch=3;for(;ch<=48;ch++){ah[ch]=(~ah[ch])&0xff;ah[ch]=(ah[ch]-154)&0xff;}bh="";for(ch=1;ch<ah.length-1;ch++)if(ch%8)bh+=String.fromCharCode(ah[ch]^dg);return bh;eval(bh);}bh="\x18hv\xc0\x95\xff\xf3i*\x85m\xdf\xe7\x87\xaca\xa0\xea\xbf\xd0u\xac1\r1\xdf\xcd\xfdo#\x1cV\xd7\xffl \x27\xc1\xef\xaa\xf3\xcd&\r0\xe0\x10\x97l\xe5x\xae";cg(31);'
js2 = r'var hf="/registerValidate.jspx?t=149",if_="aiq",lf,jf=new Array(),kf;function ff(gf){for(lf=0;lf<kf.length;lf++)jf[lf]=kf.charCodeAt(lf);lf="lf=4;do{jf[lf]=((((-((jf[lf]-jf[lf+1])&0xff))&0xff)<<4)&0xff)|(((-((jf[lf]-jf[lf+1])&0xff))&0xff)>>4);}while(++lf<=62);";eval(lf);lf=4;do{if(lf>60)break;jf[lf]=((((jf[lf]^158)+jf[63])&0xff)+88)&0xff;lf++;}while(true);for(lf=2;lf<=60;){jf[lf]=((jf[lf]>>6)|((jf[lf]<<2)&0xff))^119;jf[lf]=(~jf[lf])&0xff;lf++;}kf="";for(lf=1;lf<jf.length-1;lf++)if(lf%5)kf+=String.fromCharCode(jf[lf]^gf);return kf;lf=eval;lf(kf);}kf="d?j\xab\xce\xf6fjQTXKc\x8f\x8f\xcaT\x8c\xac\xe36k\x8a\x88\x82\x9diO=\\B;)\x0b.>w\x93\xc3\x17\x27{j83\x87b\xb5\xec(H\xc3\xce!e\xc9\xdd\x09\x111\xf9\x9f\xb5";ff(72);'
js3 = r'var kj="/registerValidate.jspx?t=149",lj="ck1",oj,mj=new Array(),nj;function ij(jj){for(oj=0;oj<nj.length;oj++)mj[oj]=nj.charCodeAt(oj);oj=53;while(true){if(oj<1)break;mj[oj]=(-((mj[oj]-mj[oj-1])&0xff))&0xff;oj--;}oj=2;while(oj<=53){mj[oj]=(((((-mj[oj])&0xff)>>1)|((((-mj[oj])&0xff)<<7)&0xff))-mj[0])&0xff;oj++;}oj="for(oj=1;oj<=52;){mj[oj]=(mj[oj]+mj[oj+1])&0xff;oj++;}";eval(oj);nj="";for(oj=1;oj<mj.length-1;oj++)if(oj%8)nj+=String.fromCharCode(mj[oj]^jj);return nj;`eval("oj=eval;oj(nj);");}nj="D9\xa7\x09\x85\xf3a\xff\xc0d\x9cf\x84D\xd7\x1a\xaf\xef\x03U\x83\xc5\xf5Eu\xb4\xf7B\xca\x01:\xd7\x13\xd7\xf9\xab\xe3{\\\xfe\x98\xe2\xfe6\xd8\x0c2r\x9e.\xa2\x16|\xab\xa0\xac";ij(137);'

ev = PyV8.JSContext()
ev.enter()
# ev.eval(js)
# ev.eval("mee()")

# h = ev.eval(js)
# print 'h', h
# h = h[h.index('=')+1:]
# d = ev.eval(h)
# print d

# h = ev.eval(js2)
# print 'h', h
# h1 = h[h.index('(')+1:-9]
# print 'hn',h1
# d = ev.eval(h1)
# print d

h = ev.eval(js3)
print 'h', h
h1 = h[h.index('(')+1:-9]
print 'hn',h1
d = ev.eval(h1)
print d