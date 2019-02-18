#!/usr/bin/env python
from re import compile as c

aircraft = {}

aircraft = [
    ['Avia B-534', c(r'b(| |-|\.)534')],
    ['Avia BH-33', c(r'bh(| |-|\.)33')],
    ['Armstrong Whitworth Scimitar', c(r'scimitar')],
    ['Blériot-SPAD S.510', c(r's(| |-|\.)510')],
    ['Boeing P-12', c(r'p(| |-|\.)12 ')],
    ['Bristol Bulldog', c(r'buldog')],
    ['Curtiss Hawk II', c(r'hawk(| |-|\.)(ii |2 )')],
    ['Curtiss Hawk III', c(r'hawk(| |-|\.)(iii |3 )')],
    ['Fairey Firefly II', c(r'firefly ii')],
    ['Fiat CR.32', c(r'cr(| |-|\.)32')],
    ['Fiat CR.42', c(r'cr(| |-|\.)42')],
    ['Gloster Gamecock II', c(r'gamecock')],
    ['Gloster Gauntlet', c(r'gauntlet')],
    ['Gloster Gladiator', c(r'gladiator')],
    ['Grumman Goblin', c(r'goblin')],
    ['Grumman F3F', c(r'f3f')],
    ['Hawker Demon', c(r'demon')],
    ['Hawker Fury', c(r'fury')],
    ['Hawker Nimrod', c('nimrod')],
    ['Heinkel He 51', c('he(| |-|\.)51')],
    ['Kawasaki Ki-10', c(r'ki(| |-|\.)10 ')],
    ['Kochyerigin DI-6', c(r'di(| |-|\.)6')],
    ['Koolhoven F.K.52', c(r'f(|\.)k(| |-|\.)52')],
    ['Polikarpov I-15',  c(r'i(| |-|\.|)15( |3|bis)')],
    
    # mono planes
    ['Arsenal VG-33', c(r'vg(| |-|\.)33')],
    ['Avia B-135', c(r'b(| |-|\.)135')],
    ['Bell P-39 Aircobra', c(r'p(| |-|\.)39')],
    ['Bell P-63 Kingcobra', c(r'p(| |-|\.)63')],
    ['Bloch MB.150-157', c(r'mb(| |-|\.)15(0|7)')],
    ['Boeing P-26 Peashooter', c(r'p(| |-|\.)26')],
    ['Breda Ba.27', c(r'ba(| |-|\.)27')],
    ['Brewster Buffalo', c(r'(f2a buffalo)|(b(| |-|\.)(2|3)39 buffalo)|(b(| |-|\.)(2|3)39)|(buffalo)|(f2a)')],
    ['CAC Boomerang', c(r'boomerang')],
    ['Caudron C.714', c('c(| |-|\.)714')],
    ['Curtiss P-36', c(r'p(| |-|\.)36')],
    ['Curtiss P-40', c(r'p(| |-|\.)40')],
    ['Curtiss-Wright CW-21', c(r'cw(| |-|\.)21')],
    ['Dewoitine D.500/D.510', c(r'd(| |-|\.)5(1|0)0')],
    ['Dewoitine D.520', c(r'd(| |-|\.)520')],
    ['Fiat G.50', c(r'g(| |-|\.)50')],
    ['Fiat G.55', c(r'g(| |-|\.)55')],
    ['Focke-Wulf Fw 190', c(r'fw(| |-|\.)190')],
    ['Focke-Wulf Ta 152', c(r'ta(| |-|\.)152')],
    ['Fokker D.XXI', c(r'd(| |-|\.)(21|xxi)')],
    ['Grumman F4F/FM Wildcat', c(r'(wildcat)|(marlet)|(f4f)')],
    ['Grumman F6F Hellcat', c(r'(f6f hellcat|hellcat|f6f)')],
    ['Grumman F8F Bearcat', c(r'(f8f bearcat)|(f8f)|(bearcat)')],
    ['Hawker Hurricane', c('hurricane')],
    ['Hawker Tempest', c('tempest')],
    ['Hawker Typhoon', c('typhoon')],
    ['Heinkel He 112', c(r'he(| |-|\.)112')],
    ['IAR 80', c(r'iar(| |-|\.)80')],
    ['Ikarus IK-2', c(r'ik(| |-|\/)2')],
    ['Kawanishi N1K/N1K-J', c(r'n1k')],
    ['Kawasaki Ki-61', c(r'ki(| |-|\.)61')],
    ['Kawasaki Ki-100', c(r'ki(| |-|\.)100')],
    ['Koolhoven F.K.58', c(r'f(|\.)k(| |-|\.)58')],
    ['Lavochkin LaGG-1', c(r'lagg(| |-|\.)1')],
    ['Lavochkin LaGG-3', c(r'lagg(| |-|\.)3')],
    ['Lavochkin La-5', c(r'la(| |-|\.)5')],
    ['Lavochkin La-7', c(r'la(| |-|\.)7')],
    ['Loire 46', c(r'loire')],
    ['Macchi C.200', c(r'c(| |-|\.)200 ')],
    ['Macchi C.202', c(r'c(| |-|\.)202 ')],
    ['Macchi C.205', c(r'c(| |-|\.)205 ')],
    ['Messerschmitt Bf 109', c(r'(me|bf)(| |-|\.)109')],
    ['Mikoyan-Gurevich MiG-1', c(r'mig(| |-|\.)1')],
    ['Mikoyan-Gurevich MiG-3',c(r'mig(| |-|\.)3')],
    ['Mitsubishi A5M', c(r'a5m')],
    ['Mitsubishi A6M Zero', c(r'(a6m zero|a6m|zero)')],
    ['Mitsubishi J2M', c(r'j2m')],
    ['Morane-Saulnier M.S.406', c(r'm(|.)s(| |-|\.)40(5|6)')],
    ['Nakajima Ki-27', c(r'ki(| |-|\.)27')],
    ['Nakajima Ki-43', c(r'ki(| |-|\.)43')],
    ['Nakajima Ki-44', c(r'ki(| |-|\.)44')],
    ['Nakajima Ki-84', c(r'ki(| |-|\.)84')],
    ['North American P-51 Mustang', c(r'(p(| |-|\.)51(.)? mustang)|(p(| |-|\.)51)|(mustang)')],
    ['Polikarpov I-16', c('i(| |-|\.)16')],
    ['PZL P.7', c(r'pzl(| |-|\.)7')],
    ['PZL P.11', c(r'pzl(| |-|\.)11')],
    ['PZL P.24', c(r'pzl(| |-|\.)24')],
    ['Reggiane Re.2000', c(r're(| |-|\.)2000')],
    ['Reggiane Re.2001', c(r're(| |-|\.)2001')],
    ['Reggiane Re.2005', c(r're(| |-|\.)2005')],
    ['Republic P-43', c(r'p(| |-|\.)43')],
    ['Republic P-47 Thunderbolt', c(r'(p(| |-|\.)47 thunderbolt)|(thunderbolt)|(p(| |-|\.)47)')],
    ['Seversky P-35', c(r'p(| |-|\.)35')],
    ['Supermarine Seafire', c(r'seafire')],
    ['Supermarine Spitfire', c('(spitfire)|(spit)')],
    ['Vought F4U/FG Corsair', c(r'(f4u corsair)|(f4u)|(corsair)')],
    ['Vultee P-66 Vanguard', c(r'(p(| |-|\.)66 vanguard)|(vanguard)|p(| |-|\.)66')],
    ['Yakovlev Yak-1', c(r'yak(| |-|\.)1')],
    ['Yakovlev Yak-3', c(r'yak(| |-|\.)3')],
    ['Yakovlev Yak-7', c(r'yak(| |-|\.)7')],
    ['Yakovlev Yak-9', c(r'yak(| |-|\.)7')],

     # heavy fighters
     ['Bell YFM-1 Airacuda', c(r'yfm(| |-|\.)1 aircuda| yfm(| |-|\.)1| aircuda')],
     ['Blackburn Roc', c('roc ')],
     ['Blackburn Skua', c('skua')],
     ['Boulton Paul Defiant', c('defiant')],
     ['Bristol Beaufighter', c(r'beaufighter')],
     ['Fairey Firefly', c(r'firefly')],
     ['Fairey Fulmar', c(r'fulmar')],
     ['Focke-Wulf Ta 154', c(r'ta(| |-|\.)154')],
     ['Fokker G.I', c(r'g(| |-|\.)(I |1 )')],
     ['Grumman F7F Tigercat', c(r'(f7f tigercat)|(f7f)|(tigercat)')],
     ['Heinkel He 219', c(r'he(| |-|\.)219')],
     ['IMAM Ro.57', c(r'ki(| |-|\.)57')],
     ['Kawasaki Ki-45', c(r'ki(| |-|\.)45')],
     ['Kawasaki Ki-102', c(r'ki(| |-|\.)102')],
     ['Lockheed P-38', c(r'(p(| |-|\.)38 lightning)|(p(| |-|\.)38)|(lightning)')],
     ['Messerschmitt Bf 110', c(r'(bf|me)(| |-|\.)110')],
     ['Messerschmitt Me 210', c(r'me(| |-|\.)210')],
     ['Messerschmitt Me 410', c(r'me(| |-|\.)410')],
     ['Mitsubishi Ki-109', c(r'ki(| |-|\.)109')],
     ['Nakajima J1N', c(r'j1n')],
     ['Northrop P-61 Black Widow', c('(p(| |-|\.)61 black widow)|(p(| |-|\.)61)|(black widow)')],
     ['Petlyakov Pe-3', c(r'pe(| |-|\.)3')],
     ['Potez 630', c('potez(| |-|\.)630')],
     ['Westland Welkin', c(r'welkin')],
     ['Westland Whirlwind',c(r'whirlwind')],

     # jet fighters
     ['Bell P-59 Airacomet', c(r'p(| |-|\.)59 aircomet|p(| |-|\.)59|aircomet')],
     ['Gloster Meteor', c(r'meteor') ],
     ['Heinkel He 162', c(r'he(| |-|\.)162') ],
     ['Lockheed P-80 Shooting Star', c(r'p(| |-|\.)80 shooting star|p(| |-|\.)80|shooting star')],
     ['Messerschmitt Me 163', c(r'me(| |-|\.)162')],
     ['Messerschmitt Me 262', c(r'me(| |-|\.)262')],
     ['Ryan FR Fireball', c(r'fireball')],

     #heavy bombers
     ['Avro Lancaster', c('lanc(aster)?')],
     ['Avro Manchester', c('manchester')],
     ['Blohm & Voss BV 142', c(r'bv(| |-|\.)142')],
     ['Boeing B-17 Flying Fortress/Fortress', c(r'b(| |-|\.)17.? ((flying )?fortress)?|(flying )?fortress')],
     ['Boeing B-29 Superfortress', c(r'b(| |-|\.)29( superfortress)?|superfortress')],
     ['Consolidated B-24 Liberator', c(r'(b(| |-|\.)24|lb(| |-|\.)30|pb4y(| |-|\.)1)( liberator)?|liberator')],
     ['Consolidated B-32 Dominator', c(r'b(| |-|\.)32( dominator)?|dominator')],
     ['Consolidated PB4Y-2 Privateer', c(r'pb4y(| |-|\.)2( privateer)?|privateer')],
     ['Farman F.221-223', c(r'f(| |-|\.)22(1|2|3)( |.)') ],
     ['Focke-Wulf Fw 200', c(r'fw(| |-|\.)200( condor)?|condor')],
     ['Handley Page Halifax', c(r'halifax')],
     ['Heinkel He 177', c(r'he(| |-|\.)177')],
     ['Petlyakov Pe-8', c(r'pe(| |-|\.)8')],
     ['Piaggio P.108', c(r'p(| |-|\.)108')],
     ['Short Stirling', c(r'stirling')],
     ['Tupolev TB-3', c('tb(| |-|\.)3')],
     ['Vickers Warwick', c(r'warwick')],

    ]