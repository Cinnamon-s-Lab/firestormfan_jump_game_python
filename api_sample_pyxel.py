import time
import firestormfan_game_api
import pyxel

#config
width = 128
height = 128
fps = 60 #0にするとfpsは無制限になります
dpc = 16 #1文字はdpc^2ピクセルを表します



App = firestormfan_game_api.App(width, height)

pyxel.init(width,height,"firestormfan",fps=fps)
pyxel.load("firestormfan_game.pyxres")

while True:
    b = time.time() #fps制限用

    #入力を与えてフレームを更新、出力する
    r = App.update(pyxel.btn(pyxel.KEY_UP),pyxel.btn(pyxel.KEY_LEFT),pyxel.btn(pyxel.KEY_RIGHT))
    #出力
    score = r['score']
    bestscore = r['bestscore']
    px = r['px']
    py = r['py']
    blocks = r['blocks']
    ground = r['ground']
    sound = r['sound']
    
    #描画処理
    pyxel.cls(12)
    for block in blocks:
        pyxel.blt(block["x"],block["y"],0,0,16,16,16)
    if ground:
        pyxel.blt(px,py,0,16,0,16,16,0)
    else:
        pyxel.blt(px,py,0,0,0,16,16,0)
    pyxel.text(width/8-1,1,str("SCORE:" + str(score)),1)
    pyxel.text(width/2,1,str("BESTSCORE:" + str(bestscore)),1)
    if sound:
        pyxel.play(0,0)
    pyxel.flip()
    #fps制限
    if fps != 0:
        while time.time()-b < 1/fps:
            pass
