import json,sys
D=sys.argv[1]
S={"V":"src/shootout21.mp4","H":"src/city_hl.mp4","I":"src/rulli_int.mp4"}
BF={"blurfit":True,"blurfit_aspect":0.75}
rows=[
# anchor, src, at, x, kind, extra, why
(None,"V",1043.6,0.74,"action",BF,"Rulli dives at De Gea's kick, Europa League final shootout 2021 (archive.org broadcast, FOX Sports feed; logo outside the crop)"),
("Back in","V",25,0.5,"action",{},"Referee and captains Fernandes and Albiol before the final's penalties (2021 broadcast)"),
("Villarreal met","V",41,0.5,"action",{},"Fernandes (United) and Albiol (Villarreal) with the referee (2021)"),
("in Gdańsk","V",98,0.72,"action",BF,"Gdańsk stadium during the shootout (2021)"),
("Gerard Moreno","V",140,0.4,"face",{},"Villarreal player in yellow, dejected, 2021 shootout (illustrative for the first goal)"),
("Edinson Cavani","V",559.3,0.45,"face",{},"Cavani #7 steps up in the shootout (2021)"),
("1-1 after","V",163,0.72,"action",BF,"A penalty in the 2021 shootout (wide)"),
("And nobody","V",300,0.72,"action",BF,"Rulli in goal, FedEx boards (2021)"),
("Five each","V",360,0.72,"action",BF,"Shootout with scoreboard dots (2021)"),
("Then ten","V",540,0.72,"action",BF,"Shootout with the dots filling (2021)"),
("Every outfield","V",400.3,0.45,"face",{},"Bruno Fernandes, who scored (2021)"),
("So it came","V",120,0.5,"action",{},"De Gea and Rulli with the referee before the keepers' kicks (2021)"),
("Villarreal's Gerónimo","V",1024.1,0.62,"action",{},"Rulli takes his kick (2021)"),
("Then David","V",1036.5,0.5,"face",{},"De Gea about to take his kick (2021)"),
("He hadn't saved a single","V",499,0.5,"action",{},"De Gea in goal, back to camera (2021)"),
("In fact","V",859,0.5,"action",{},"De Gea diving, beaten (earlier kick; 2021)"),
("since April","V",239.9,0.5,"face",{},"De Gea in goal (2021)"),
("Rulli dived","V",1044.4,0.74,"action",dict(BF,speed=0.5,replay=True),"REPLAY: Rulli's dive, half speed (same footage as frame 1)"),
("11-10","V",1119.3,0.5,"action",{},"Broadcast graphic: Villarreal win 11-10 after penalties (2021)"),
("Twenty-one penalties","V",640,0.5,"action",{},"United fan holds a scarf during the shootout (2021)"),
("and the twenty-second","V",1062.0,0.45,"face",{},"De Gea, beaten (2021)"),
("It gave Villarreal","V",1052.4,0.5,"action",{},"Villarreal celebrate (2021)"),
("European trophy","V",1056.6,0.5,"action",{},"Villarreal celebrate; broadcast caption 'Villarreal campeon de la Europa League 2020/21'"),
("This summer","I",20,0.5,"face",{},"Rulli in City kit after the Brighton game (2026, City's own interview). Illustrative for the summer signing"),
("from Marseille","H",56.0,0.5,"action",{},"Match action, Man City v Brighton (illustrative)"),
("as Donnarumma's","I",60,0.5,"face",{},"Rulli, City backup keeper (2026)"),
("In October","H",8.0,0.5,"action",{},"Etihad, City v Brighton, Oct 28 2026"),
("City were the League","H",76.0,0.3,"action",BF,"Carabao Cup boards at the Etihad (shootout start)"),
("at home","H",3.0,0.5,"action",{},"City v Brighton at the Etihad (broadcast bug names both teams)"),
("They came from","H",52.0,0.5,"face",{},"Brighton's goal, City behind (2026 highlights)"),
("twice to draw","H",66.6,0.5,"action",{},"City players celebrate an equaliser, score bug 2-2"),
("Another shootout","H",77.0,0.3,"action",BF,"The shootout begins (2026)"),
("Mateo","H",113.1,0.5,"face",{},"Kovacic before his kick (2026)"),
("penalty was saved","H",115.3,0.3,"action",BF,"Kovacic's kick saved by Steele (2026)"),
("and City fell","H",118.0,0.5,"face",{},"Brighton keeper Steele (2026)"),
("Then Rulli saved","H",120.3,0.3,"action",BF,"Ayari's kick (2026)"),
("Yasin Ayari","H",122.8,0.3,"action",BF,"Rulli saves Ayari's kick (2026)"),
("Lewis Dunk","H",133.2,0.3,"action",BF,"Dunk's kick saved by Rulli (2026)"),
("City won","H",141.3,0.5,"action",{},"Rulli embraced after the shootout (2026)"),
("But here's","I",90,0.5,"face",{},"Rulli (2026 interview)"),
("City had him","I",38,0.5,"face",{},"Rulli in City kit (illustrative for his first spell)"),
("back in 2016","I",110,0.5,"face",{},"Rulli in City kit (illustrative; no 2016 footage found)"),
("He spent","H",145.0,0.5,"action",{},"City celebrate the shootout (2026)"),
("without a single","I",150,0.5,"face",{},"Rulli, City backup (2026)"),
]
shots=[]
for i,(a,src,at,x,kind,ex,why) in enumerate(rows,1):
    s={"clip":f"M{i:02d}","src":src,"at":at,"x":x,"kind":kind}
    s.update(ex)
    if a: s["anchor"]=a
    s["why"]=why
    shots.append(s)
json.dump({"sources":S,"promise":["penalty","penalties","shootout","saved","Rulli"],"shots":shots},open(D+"/cuts_plan.json","w",encoding="utf-8"),indent=1,ensure_ascii=False)
