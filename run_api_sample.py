import time
import firestormfan_game_api
import keyboard

#config
width = 128
height = 128
fps = 60 #0にするとfpsは無制限になります
dpc = 16 #1文字はdpc^2ピクセルを表します



App = firestormfan_game_api.App(width, height)


while True:
    b = time.time() #fps制限用

    #入力を与えてフレームを更新、出力する
    r = App.update(keyboard.is_pressed("UP"),keyboard.is_pressed("LEFT"),keyboard.is_pressed("RIGHT"))
    #出力
    score = r['score']
    bestscore = r['bestscore']
    player_x = r['px']
    player_y = r['py']
    blocks = r['blocks']
    ground = r['ground']
    sound = r['sound']
    
    #描画処理
    for_show_player = [["・" for i in range(width//dpc)] for j in range(height//dpc)]
    for_show_blocks = [["・" for i in range(width//dpc)] for j in range(height//dpc)]
    if player_x >= 0 and player_x < width and player_y >= 0 and player_y < height:
        for_show_player[int(player_y/dpc)][int(player_x/dpc)] = "＠"
    print_queue = []
    print_queue.append(f"score:{r['score']},bestscore:{r['bestscore']}")
    
    for block in blocks:
        if block['x'] >= 0 and block['x'] < width and block['y'] >= 0 and block['y'] < height:
            for_show_blocks[int(block['y']/dpc)][int(block['x']/dpc)] = "＃"
    
    for show_player,show_block in zip(for_show_player,for_show_blocks):
        xli = []
        for pl,bl in zip(show_player,show_block):
            if pl=="・":
                if bl=="＃":
                    xli.append("＃")
                elif pl=="＠":
                    xli.append("＠")
                else:
                    xli.append("・")
            else:
                xli.append(pl)
        print_queue.append("".join(xli))

    #表示
    printstr ="\n"+"\n".join(print_queue)
    print(printstr,end="")
    
    #fps制限
    if fps != 0:
        while time.time()-b < 1/fps:
            pass
