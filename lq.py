from manim import *


'''
1、准备4张扑克牌动画：首先，展示4张任意的扑克牌，然后通过动画效果展示它们被洗乱的过程。
2、对折并撕成两半：展示每张牌对折并撕成两半的动画，之后将它们叠放在一起，形成ABCD-ABCD的序列。
3、根据名字的字数调整牌序：模拟将顶部的几张牌移至底部的动画。此步骤可通过文本提示来简化表示，不需具体实现根据不同名字字数的变化。
4、将顶部3张牌随机插入中间：展示将顶部的3张牌拿出并随意插入到牌堆中间的动画。
5、藏牌动作：模拟将顶部的一张牌藏到屁股下的动画。
6、根据地区调整牌序：展示根据用户是南方人、北方人还是不确定的情况，将不同数量的牌从顶部插入到中间的动画。
7、根据性别洒牌：模拟根据用户性别，从顶部拿出不同数量的牌并洒到空中的动画。
8、念咒语调整牌序：展示口中念“见证奇迹的时刻”，同时将顶部的牌移到底部的动画，根据性别决定重复的次数。
9、喊口号并调整牌序：按照喊口号“好运留下来！”和“烦恼丢出去！”的指示，展示将顶上的牌放到底层或扔到空中的动画，根据性别决定循环的次数。
10、揭示魔术结果：展示剩下的牌与屁股下的牌相同，完成魔术的动画。
'''

class PokerTrick(Scene):
    def construct(self):
        # 定义牌的大小和颜色
        card_width = 1
        card_height = 1.5
        card_color = WHITE

        # 创建四张牌
        suits = ["♠", "♥", "♣", "♦"]
        cards = VGroup(*[
            Rectangle(width=card_width, height=card_height, color=card_color).set_fill(card_color, opacity=1).set_stroke(WHITE, 1).add(Text(suit, color=BLACK).move_to(card.get_center()))
            for suit, card in zip(suits, [Rectangle(width=card_width, height=card_height) for _ in suits])
        ])

        # 排列牌
        cards.arrange(RIGHT, buff=0.5)

        # 展示牌
        self.play(LaggedStart(*[DrawBorderThenFill(card) for card in cards], lag_ratio=0.5))
        self.wait(1)

         # 洗牌动画：随机改变牌的位置
        cards.shuffle()
        self.play(*[ApplyMethod(card.move_to, new_pos) for card, new_pos in zip(cards, [1.4 * UP, UP+LEFT*1.2, DOWN*0.9+RIGHT*0.6, 1.6 * DOWN+0.2*LEFT])], run_time=1.5)
        self.wait(0.5)

        # 将牌重新排列以进入下一步
        self.play(cards.animate.arrange(RIGHT, buff=0.5).move_to(ORIGIN))
   
        new_suits = ["A", "B", "C", "D"]

        # 替换文字内容
        self.play(*[Transform(card[1], Text(new_suit, color=BLACK).move_to(card.get_center())) for card, new_suit in zip(cards, new_suits)])
        self.wait(0.5)
        # 左移
        self.play(*[ApplyMethod(card.move_to, card.get_center() + LEFT * 3 ) for card in cards])



        # 定义ABCD文本对象并放置在牌的中心位置
        text_A = Text("A").move_to(cards[0].get_center())
        text_B = Text("B").move_to(cards[1].get_center() )
        text_C = Text("C").move_to(cards[2].get_center() )
        text_D = Text("D").move_to(cards[3].get_center() )



        # 添加ABCD文本对象到场景中
        self.add(text_A, text_B, text_C, text_D)
        self.play(FadeOut(cards), runtime = 2)


        self.play(
            ApplyMethod(text_B.shift, 0.2*LEFT),
            ApplyMethod(text_C.shift, 0.4*LEFT),
            ApplyMethod(text_D.shift, 0.6*LEFT),
            run_time=1
        )
        


        # 定义新的ABCD文本对象并放置在旧的ABCD文本对象下方
        text_A_new = Text("A").move_to(text_A.get_center())
        text_B_new = Text("B").move_to(text_B.get_center())
        text_C_new = Text("C").move_to(text_C.get_center())
        text_D_new = Text("D").move_to(text_D.get_center())

        # 下移一单位
        self.play(
            ApplyMethod(text_A_new.shift, DOWN),
            ApplyMethod(text_B_new.shift, DOWN),
            ApplyMethod(text_C_new.shift, DOWN),
            ApplyMethod(text_D_new.shift, DOWN),
            run_time=1
        )

        text_A_center = text_A.get_center()
        text_B_center = text_B.get_center()
        text_C_center = text_C.get_center()
        text_D_center = text_D.get_center()


        # 计算文本对象的中心关于y轴的对称位置
        A_symmetric = np.array([-text_A_center[0], 0, 0])
        B_symmetric = np.array([-text_B_center[0], 0, 0])
        C_symmetric = np.array([-text_C_center[0], 0, 0])
        D_symmetric = np.array([-text_D_center[0], 0, 0])

        # 对称

        move_text_A = text_A_new.animate.move_to(D_symmetric)
        move_text_B = text_B_new.animate.move_to(C_symmetric)
        move_text_C = text_C_new.animate.move_to(B_symmetric)
        move_text_D = text_D_new.animate.move_to(A_symmetric)

        # 播放动画
        self.play(move_text_A, move_text_B, move_text_C, move_text_D)



        # 创建箭头对象
        arrow = CurvedArrow(start_point=text_A.get_bottom(), end_point=text_A_new.get_bottom(), color=RED)     
        
        cir1 = Circle(radius=0.6, color=RED).move_to(text_B_center)
        cir2 = Circle(radius=0.6, color=RED).move_to(text_C_center)
        cir3 = Circle(radius=0.6, color=RED).move_to(text_D_center)
                # 将所有对象放入VGroup
        vgroup = VGroup(arrow, cir1, cir2, cir3)
        
        
        self.play(Create(vgroup))
        self.wait(1)



        self.play(

            FadeOut(vgroup)
        )





        # 绘制圈
        
        ellipse = Ellipse(width=3.5, height=2, color=RED).move_to(text_B_center)

        
        
        arrow1 = CurvedArrow(ellipse.get_right(), np.array([(-text_D_center[0]-text_C_center[0])/2, 0, 0]), color=BLUE, angle=TAU/4)
        arrow2 = CurvedArrow(ellipse.get_right(), np.array([(-text_B_center[0]-text_C_center[0])/2, 0, 0]),  color=BLUE, angle=TAU/4)
        arrow3 = CurvedArrow(ellipse.get_right(), np.array([(-text_A_center[0]-text_B_center[0])/2, 0, 0]),  color=BLUE, angle=TAU/4)
        
        # 添加元素、圈和箭头到画面中
        self.add( ellipse)
        self.play(Create(arrow1))
        self.wait(0.5)
        self.play(Transform(arrow1, arrow2))
        self.wait(0.5)
        self.play(Transform(arrow1, arrow3))


        self.play(
            Transform(text_D, text_D.copy().scale(1.5).set_color(YELLOW)),
            Transform(text_D_new, text_D_new.copy().scale(1.5).set_color(YELLOW))
        )
                # 创建新的文本元素并替换原来的文本元素
        text_q1 = Text("1", color=WHITE).move_to(text_B_center)
        text_q2 = Text("2", color=WHITE).move_to(text_C_center)
        text_q3 = Text("3", color=WHITE).move_to(text_D_center)
        text_q4 = Text("4", color=WHITE).move_to(D_symmetric)
        text_q5 = Text("5", color=WHITE).move_to(C_symmetric)
        text_q6 = Text("6", color=WHITE).move_to(B_symmetric)

        self.play(FadeOut(arrow1),FadeOut(ellipse),
                    ReplacementTransform(text_B, text_q1),
                    ReplacementTransform(text_C, text_q2),
                    ReplacementTransform(text_A, text_q3),
                    ReplacementTransform(text_C_new, text_q4),
                    ReplacementTransform(text_B_new, text_q5),
                    ReplacementTransform(text_A_new, text_q6),
                  text_D.animate.move_to(text_A_center),
                  runtime = 2
                  )
        
        self.play( text_D.animate.shift(DOWN*2+LEFT*0.3))

        # 创建矩形框并添加到场景中
        rect = SurroundingRectangle(text_D, buff=0.1)
        self.play(Create(rect)) 
        self.wait(1)



        self.play(text_D_new.animate.scale(1.5))
        self.play(text_D_new.animate.scale(1/1.5))

        self.wait(1)

        

        
        text_m = Text("男", color=WHITE ,font_size=32).move_to(text_A_center + LEFT * 0.3 + UP*2)
        text_fm = Text("女", color=WHITE ,font_size=32).move_to(text_A_center +  LEFT * 0.3)
        text_q1_copy = text_q1.copy()
        text_q2_copy = text_q2.copy()
        text_q3_copy = text_q3.copy()
        text_q4_copy = text_q4.copy()
        text_q5_copy = text_q5.copy()
        text_q6_copy = text_q6.copy()
        text_D_copy  = text_D_new.copy()

        # 将复制的元素移动到原有位置的上方
        text_q1_copy.shift(UP * 2)
        text_q2_copy.shift(UP* 2)
        text_q3_copy.shift(UP* 2)
        text_q4_copy.shift(UP* 2)
        text_q5_copy.shift(UP* 2)
        text_q6_copy.shift(UP* 2)
        text_D_copy.shift(UP* 2)



        self.play(FadeIn(text_q1_copy), FadeIn(text_q2_copy), FadeIn(text_q3_copy),
                  FadeIn(text_q4_copy), FadeIn(text_q5_copy), FadeIn(text_q6_copy) ,FadeIn(text_D_copy),
                  FadeIn(text_m), FadeIn(text_fm))
        
        
        # 添加删除线，假设删除线的起始点为文本的左上角，终止点为文本的右下角
        delete_line_m_1 = Line(text_q1_copy.get_corner(UL), text_q1_copy.get_corner(DR),color=RED)

        delete_line_fm_1 = Line(text_q1.get_corner(UL), text_q1.get_corner(DR),color=RED)
        delete_line_fm_2 = Line(text_q2.get_corner(UL), text_q2.get_corner(DR),color=RED)

        # 将文本和删除线添加到场景中
        self.play(FadeIn(delete_line_m_1), FadeIn(delete_line_fm_1), FadeIn(delete_line_fm_2))
        self.play(FadeOut(delete_line_m_1), FadeOut(delete_line_fm_1), FadeOut(delete_line_fm_2),
                  FadeOut(text_q1), FadeOut(text_q2), FadeOut(text_q1_copy),

                  )
        



        #  1
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q3.animate.move_to(text_D_new.get_center() ),
            ApplyMethod(text_q4.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q2_copy.animate.move_to(text_D_copy.get_center() ),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )
        # 2
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q4.animate.move_to(text_q3.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q3_copy.animate.move_to(text_q2_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )
        # 3
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q5.animate.move_to(text_q4.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q4.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q4_copy.animate.move_to(text_q3_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )
        # 4
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q6.animate.move_to(text_q5.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q4.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q5_copy.animate.move_to(text_q4_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )
        # 5
        self.play(
            ApplyMethod(text_q6.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_D_new.animate.move_to(text_q6.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q4.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q6_copy.animate.move_to(text_q5_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            
        )
        # 6
        self.play(
            ApplyMethod(text_q4.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q3.animate.move_to(text_D_new.get_center() ),
            ApplyMethod(text_D_new.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_q6_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_D_copy.animate.move_to(text_q6_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            
        )
        # 7
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q4.animate.move_to(text_q3.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q5.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q2_copy.animate.move_to(text_D_copy.get_center() ),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )
        self.wait(2)




        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))

        # h1
        self.play(
            ApplyMethod(text_D_new.shift, LEFT*1.2),
            # ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_q5.animate.move_to(text_q4.get_center() ),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            ApplyMethod(text_q4.shift, LEFT*1.2 ),
            ApplyMethod(text_q6.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            # ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            text_q3_copy.animate.move_to(text_q2_copy.get_center() ),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            ApplyMethod(text_q4_copy.shift, LEFT*1.2),
            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            
        )

        self.wait(2)

        #f1
        
        text_next_2 = Text("烦恼丢出去！", color=BLUE, font_size=30).next_to(ORIGIN, DOWN*2)


        delete_line_m_2 = Line(text_q4_copy.get_corner(UL), text_q4_copy.get_corner(DR),color=RED)
        delete_line_fm_3 = Line(text_q6.get_corner(UL), text_q6.get_corner(DR), color=RED)

        self.play(
            FadeIn(delete_line_fm_3 ,delete_line_m_2 ), Transform(text_next, text_next_2)
        )
        self.play(FadeOut(delete_line_fm_3 ,delete_line_m_2), FadeOut(text_q4_copy, text_q6))
        self.wait(1)



        # h2

        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))


        self.play(
            ApplyMethod(text_q5.shift, LEFT*1.2),
            ApplyMethod(text_q3.shift, LEFT*1.2 ),
            text_D_new.animate.move_to(text_q5.get_center()  ),
            
            ApplyMethod(text_q4.shift, LEFT*1.2 ),

            ApplyMethod(text_D_copy.shift, LEFT*1.2 ),
            ApplyMethod(text_q6_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            text_q5_copy.animate.move_to(text_q3_copy.get_center()),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),
            
            
        )

        text_next_2 = Text("烦恼丢出去！", color=BLUE, font_size=30).next_to(ORIGIN, DOWN*2)


        #f2
        delete_line_m_3 = Line(text_q6_copy.get_corner(UL), text_q6_copy.get_corner(DR),color=RED)
        delete_line_fm_4 = Line(text_q3.get_corner(UL), text_q3.get_corner(DR), color=RED)

        self.play(
            FadeIn(delete_line_m_3 ,delete_line_fm_4,  ), Transform(text_next, text_next_2)
        )
        self.play(FadeOut(delete_line_m_3 ,delete_line_fm_4), FadeOut(text_q6_copy, text_q3))
        self.wait(1)


        
        # h3

        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))


        self.play(
            ApplyMethod(text_q5.shift, LEFT*1.2),
            ApplyMethod(text_D_new.shift, LEFT*1.2 ),
            text_q4.animate.move_to(text_D_new.get_center() ),

            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            text_D_copy.animate.move_to(text_q5_copy.get_center()),
            ApplyMethod(text_q2_copy.shift, LEFT*1.2),  
        )
        
        text_next_2 = Text("烦恼丢出去！", color=BLUE, font_size=30).next_to(ORIGIN, DOWN*2)


        #f3
        delete_line_m_3 = Line(text_q2_copy.get_corner(UL), text_q2_copy.get_corner(DR),color=RED)
        delete_line_fm_4 = Line(text_q5.get_corner(UL), text_q5.get_corner(DR), color=RED)

        self.play(
            FadeIn(delete_line_m_3 ,delete_line_fm_4 ), Transform(text_next, text_next_2)
        )
        self.play(FadeOut(delete_line_m_3 ,delete_line_fm_4), FadeOut(text_q2_copy, text_q5))
        self.wait(1)

        
        # h4

        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))


        self.play(
            ApplyMethod(text_q4.shift, LEFT*1.2),
            ApplyMethod(text_D_new.shift, LEFT*1.2 ),
            text_D_new.animate.move_to(text_q4.get_center() ),

            ApplyMethod(text_q5_copy.shift, LEFT*1.2),
            ApplyMethod(text_D_copy.shift, LEFT*1.2),  
            text_q3_copy.animate.move_to(text_D_copy.get_center()),
            
        )
        
        text_next_2 = Text("烦恼丢出去！", color=BLUE, font_size=30).next_to(ORIGIN, DOWN*2)


        #f4
        delete_line_m_3 = Line(text_q5_copy.get_corner(UL), text_q5_copy.get_corner(DR),color=RED)
        delete_line_fm_4 = Line(text_q4.get_corner(UL), text_q4.get_corner(DR), color=RED)

        self.play(
            FadeIn(delete_line_m_3 ,delete_line_fm_4 ), Transform(text_next, text_next_2)
        )
        self.play(FadeOut(delete_line_m_3 ,delete_line_fm_4), FadeOut(text_q5_copy, text_q4))
        self.wait(1)


        
        
        # h5

        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))


        self.play(
            
            # text_D_new.animate.move_to(ORIGIN) ,
        
            ApplyMethod(text_q3_copy.shift, LEFT*1.2),
            text_D_copy.animate.move_to(text_q3_copy.get_center()),
            
        )
        
        text_next_2 = Text("烦恼丢出去！", color=BLUE, font_size=30).next_to(ORIGIN, DOWN*2)


        #f4
        delete_line_m_3 = Line(text_q3_copy.get_corner(UL), text_q3_copy.get_corner(DR),color=RED)


        self.play(
            FadeIn(delete_line_m_3  ), Transform(text_next, text_next_2)
        )
        self.play(FadeOut(delete_line_m_3 ), FadeOut(text_q3_copy))
        self.wait(1)


        # h5

        text_center = text_q4_copy.get_center()
        text_next = Text("好运留下来！", color=RED_B, font_size=30).next_to(text_center, UP *2)
        self.play(FadeIn(text_next))


        self.play(  
            FadeOut(rect),
            text_D_new.animate.move_to(ORIGIN) ,
            text_D_copy.animate.move_to(ORIGIN) ,
            text_D.animate.move_to(ORIGIN) ,
        )
       
        



        
