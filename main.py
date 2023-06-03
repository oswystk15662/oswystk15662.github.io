import cgi, cgitb, sys
# CGIモジュールのインポート

import src.femurRo,src.femurCT,src.kneeRo,src.kneeCT

cgitb.enable() # デバッグに使うので、本番環境では記述しない

form = cgi.FieldStorage() # フォームデータを取得する

mode = form.getfirst("mode")
part = form.getfirst("part")
implant = form.getvalue("implant")

if mode == 'CT':
    if part == 'femur':
        src.femurRo.Run()
    elif part == 'knee':
        src.femurRo.Run()