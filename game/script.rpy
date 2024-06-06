# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define w = Character('Алиса', color="#FFD700")
define m = Character('Элиас', color="#FFD700")
define org = Character('Организатор', color="#FFD700")
define morg = Character('Мартин', color="#FFD700")
define t = Character('Тестировщик', color="#FFD700")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
#For example, we might want to have text that is {b}bold{/b}, {i}italic{/i}, {s}struckthrough{/s}, or {u}underlined{/u}.
 
# чтобы поменять шрифт: "The font tag changes the font, for example to {font=DejaVuSans-Bold.ttf}DejaVuSans-Bold.ttf{/font}"
#The p tag breaks a paragraph,{p}and waits for the player to click." If it is given a number as an argument,{p=1.5}it waits that many seconds."
#     $ variable = "{i}значение переменной{/i}" "For example, this displays the [variable]." 
# \"Визуальные Новеллы\"
 


# Игра начинается здесь:
init:
    image scene_1_1 = im.Scale("Images/background_part1/palatka.jpg", 1280, 720)
    image warrior = "Images/character_part1/warrior.jpg"

    image scene_1_2 = im.Scale("Images/background_part1/black.jpg", 1280, 720)
    image scene_1_2_room = im.Scale("Images/background_part1/room.jpg", 1280, 720)

    image scene_1_3_turniket = im.Scale("Images/background_part1/turniket.jpg", 1280, 720)
    image scene_1_3_holl = im.Scale("Images/background_part1/holl.jpg", 1280, 720)
    image scene_1_3_balkon = im.Scale("Images/background_part1/balkon.jpg", 1280, 720)

    # Aлиса
    image alice = "Images/character_part1/alice.jpg"
    image alicer = "Images/character_part1/alice_real.jpg"
    image alice_sad = "Images/character_part1/alice_sad.jpg"
    image alice_funny = "Images/character_part1/alice_smile.jpg"
    image alice_scared = "Images/character_part1/alice_scared.jpg"
    image alice_stressful = "Images/character_part1/alice_stress.jpg"
    image alice_blushed = "Images/character_part1/alice_blushed.jpg"
    image alice_angry = "Images/character_part1/alice_angry.jpg"
    image alice_sad_r = "Images/character_part1/alice_sad_r.jpg"
    image alice_funny_r = "Images/character_part1/alice_smile_r.jpg"
    image alice_scared_r = "Images/character_part1/alice_scared_r.jpg"
    image alice_stressful_r = "Images/character_part1/alice_stress_r.jpg"
    image alice_blushed_r = "Images/character_part1/alice_blushed_r.jpg"
    image alice_angry_r = "Images/character_part1/alice_angry_r.jpg"


    # Элиас
    image alias = "Images/character_part1/alias.jpg"
    image aliasr = "Images/character_part1/alias_real.jpg"
    image alias_sad = "Images/character_part1/alias_sad.jpg"
    image alias_funny = "Images/character_part1/alias_smile.jpg"
    image alias_scared = "Images/character_part1/alias_scared.jpg"
    image alias_stressful = "Images/character_part1/alias_stress.jpg"
    image alias_blushed = "Images/character_part1/alias_blushed.jpg"
    image alias_angry = "Images/character_part1/alias_angry.jpg"
    image alias_sad_r = "Images/character_part1/alias_sad_r.jpg"
    image alias_funny_r = "Images/character_part1/alias_smile_r.jpg"
    image alias_scared_r = "Images/character_part1/alias_scared_r.jpg"
    image alias_stressful_r = "Images/character_part1/alias_stress_r.jpg"
    image alias_blushed_r = "Images/character_part1/alias_blushed_r.jpg"
    image alias_angry_r = "Images/character_part1/alias_angry_r.jpg"

    # Организатор
    image org = "Images/character_part1/org.jpg"
    image org_funny = "Images/character_part1/org_smile.jpg"
    image org_stressful = "Images/character_part1/org_stress.jpg"

    # Взломщик
    image vzlom = "Images/character_part1/vzlom.jpg"
    image vzlomr = "Images/character_part1/vzlom_r.jpg"
    image vzlomr_funny = "Images/character_part1/vzlom_smile.jpg"
    image vzlomr_stressful = "Images/character_part1/vzlom_stress.jpg"

    
label start:


    scene scene_1_1

    show warrior at right

    "???" "Эй, ты, давай в атаку, что сидишь прячешься?"
    hide warrior

    "Мое тело не двигается."

    "Пытаюсь пошевелить пальцами, но они только сильнее всаживаются в мокрую землю. Она противно чавкает, но поддается под действием силы."

    "Мои глаза спускаются вниз, секунда, и горло пересыхает, а тошнота подкатывает мгновенно. Земля перемешана не с влагой, которую дал дождь, а с кровью, самой настоящей кровью."
    
    "Мой крик слышится как будто бы со стороны. Я не узнаю свой мелодичный голос, которым пою в хоре, это надорвавшийся, полный отчаяния тембр."

    "От страха кидаюсь в сторону, но наталкиваюсь на груду щитов и отполированных шлемов."

    "В панике взявшись за один из них, я разглядываю свое отражение."

    menu:
        "Я..."
        "был мужчиной.":    
            $ woman = False
        "была женщиной.":
            $ woman = True
    
    if woman == False:
        jump man
    else:
        jump woman
#     hide scene_1_1

# label scene_1_2:
#     scene scene_1_2
#     "Проснулась."
#     scene scene_1_2_room with fade
#     "Резкий и судорожный вдох. Я была в своей постели. Руки нащупали грудину и.. не нашли ничего особенного." 
#     "Это сон, просто сон, не верилось." 
#     "Встала, босые ноги коснулись прохладного пола, а голова пронзила болью. Не нужно было вчера играть допоздна в бета-версию игры." 
#     "Как всегда оставила все на конец и вот результат - невыспавшееся лицо смотрело на меня по другую сторону зеркала в ванной. Надо было срочно привести себя в порядок, иначе поеду в офис игровой компании как зомби."
#     "Как получила ссылку для скачивания - моя жадность перекрыла качество ответственного работника и я долго откладывала начало работы над тестировкой, чтобы растянуть удовольствие от прохождения."
#     "Да так растянула, что пришлось судорожно-обморочно проходить ровно за 12 часов до закрытой встречи компании." 
#     "Благо, я умею быстро и качественно находить любые баги, поэтому таблица ошибок была готова уже к утру."

#     show alicer at left
#     w "Пару часов на сон и я как огурчик." 
#     hide alicer
#     "Были мои слова, когда я улыбалась, лежа в кровати."
#     "Но это было ОШИБКОЙ."
#     "Утром времени, чтобы собраться,тоже не хватало. Его оставалось, все меньше и меньше, поэтому я решила, что завтрака сегодня не будет."

#     menu:
#         show alicer at left
#         "Нечего расстраиваться."
#         "Свожу себя на ужин в какое-нибудь кафе, позову заодно подругу с собой.":
#             pass
#         "Закажу еды на дом и включу сериалы. Вот и награда.":
#             pass
#     hide alicer
#     "Удовлетворившись решением, я открыла шкаф. Там ждал подготовленный костюм, который я купила на заказ."
#     "Он отсылал на одежду главного героя игры. Я начала фанатеть по этой игре уже после анонса, а уж когда узнала, что вхожу в узкий круг лиц, кто “пощупает” новеллу самыми первыми - совсем сошла с ума."
#     "Скупив постеры с маркетплейсов и повесив их над кроватью, я поняла, что для полного счастья мне не хватало только закосплеить главного героя прямо на собрании после тестировки."
#     "Мне действительно понравилась графика, все выглядело настолько реальным, что иногда я забывала, что сижу на диване в своей маленькой съемной квартирке перед телевизором с джойстиком в руках."
    
#     menu:
#         show alicer at left
#         "Интересно, хотелось бы мне оказаться в том мире по-настоящему?"
#         "Было бы интересно.":
#             $ reaction1_1 = True
#         "Даже и не знаю, скорее нет.":
#             $ reaction1_1 = Fasle
#     hide alicer
#     "Когда я примерила наряд главной героини - меня посетило странное ощущение. Слишком уж натурально все выглядело. Но все же я почувствовала себя слишком неловко в нем."
#     "Как-то странно, что взрослая девушка идет на рабочую встречу в костюме героя, как ребенок. Надо было решить."
    
#     menu:
#         show alice at left
#         "Я решила надеть..."
#         "Косплей.":
#             $ cosplay = True
#         "Обычную одежду.":
#             $ cosplay = False
#     hide alice
#     "Разгладив складки и поправив пряди в косичке, я улыбнулась отражению."
#     if cosplay ==True:
#         show alice at left
#         w "Ты неотразима"
#         hide alice
#     else:
#         show alicer at left
#         w "Ты неотразима"
#         hide alicer
#     "Я стрельнула в зеркало из пальцев и сдула невидимый дым с “пистолета”. Настоящее рембо, которое покорит всех организаторов."
#     "Так, все, надо бежать. Я вышла за дверь."



    
    return
    # menu:

    #     "Да.":
    #         jump choice1_yes

    #     "Нет.":
    #         jump choice1_no

    # label choice1_yes:

    #     $ menu_flag = True

    #     e "While creating a multi-path visual novel can be a bit more work, it can yield a unique experience."

    #     jump choice1_done

    # label choice1_no:

    #     $ menu_flag = False

    #     e "Games without menus are called kinetic novels, and there are dozens of them available to play."

    #     jump choice1_done

    # label choice1_done:

    #     # ... the game continues here.
 
