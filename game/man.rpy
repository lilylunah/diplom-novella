label man:
    "Темные волосы были взъерошены и вымазаны в чем-то липком и темном. Зажмурившись, я подумал, что даже не хочу знать в чем они испачканы."

    "Тот воин, который пытался смотивировать меня драться, видимо одолел одного из своих противников и был готов уже подойти, чтобы встряхнуть меня и вернуть сознание в мою голову, но опоздал."
    
    "В грудь, ровно в солнечное сплетение, прилетела стрела."

    "Я не сразу понимаю, что звук остановился где-то ниже моего подбородка."

    "Боли нет, только ощущение, что что-то идет не так."

    "Взгляд опускается на древко с ярким оперением торчащим прямо из легких доспехов, надетых на меня. Мои сухие губы произносят короткое “что”, а руки резко вытягивают стрелу из плоти, как я…"
hide scene_1_1

label scene_1_2m:
    scene scene_1_2
    "Проснулся."
    scene scene_1_2_room with fade
    "Резкий и судорожный вдох. Я был в своей постели. Руки нащупали грудину и.. не нашли ничего особенного." 
    "Это сон, просто сон, не верилось." 
    "Встал, босые ноги коснулись прохладного пола, а голова пронзила болью. Не нужно было вчера играть допоздна в бета-версию игры." 
    "Как всегда оставил все на конец и вот результат - невыспавшееся лицо смотрело на меня по другую сторону зеркала в ванной. Надо было срочно привести себя в порядок, иначе поеду в офис игровой компании как зомби."
    "Как получил ссылку для скачивания - моя жадность перекрыла качество ответственного работника и я долго откладывал начало работы над тестировкой, чтобы растянуть удовольствие от прохождения."
    "Да так растянул, что пришлось судорожно-обморочно проходить ровно за 12 часов до закрытой встречи компании." 
    "Благо, я умею быстро и качественно находить любые баги, поэтому таблица ошибок была готова уже к утру."

    show alias at left
    m "Пару часов на сон и я как огурчик." 
    hide alias
    "Были мои слова, когда я улыбался, лежа в кровати."
    "Но это было ОШИБКОЙ."
    "Утром времени, чтобы собраться,тоже не хватало. Его оставалось, все меньше и меньше, поэтому я решил, что завтрака сегодня не будет."
    show alias at left
    menu:
        m "Нечего расстраиваться."
        "Схожу в какой-нибудь бар, позову заодно друга с собой.":
            pass
        "Закажу еды на дом и включу сериалы. Вот и награда.":
            pass
    hide alias
    "Удовлетворившись решением, я открыл шкаф. Там ждал подготовленный костюм, который я купил на заказ."
    "Он отсылал на одежду главного героя игры. Я начал фанатеть по этой игре уже после анонса, а уж когда узнал, что вхожу в узкий круг лиц, кто “пощупает” новеллу самыми первыми - совсем сошел с ума."
    "Скупив постеры с маркетплейсов и повесив их над кроватью, я понял, что для полного счастья мне не хватало только закосплеить главного героя прямо на собрании после тестировки."
    "Мне действительно понравилась графика, все выглядело настолько реальным, что иногда я забывал, что сижу на диване в своей маленькой съемной квартирке перед телевизором с джойстиком в руках."
    show alias at left
    menu:
        m "Хм, а хотелось бы мне оказаться в том мире по-настоящему?"
        "Было бы интересно.":
            $ reaction1_1 = True
        "Даже и не знаю, скорее нет.":
            $ reaction1_1 = False
    hide alias
    "Когда я примерил наряд главного героя - меня посетило странное ощущение. Слишком уж натурально все выглядело. Но все же я почувствовал себя неловко в нем."
    "Как-то странно, что взрослый парень идет на рабочую встречу в костюме героя, как ребенок. Надо было решить."
    show alias at left
    menu:
        m "Я решил надеть..."
        "Косплей.":
            $ cosplay = True
        "Обычную одежду.":
            $ cosplay = False
    hide alias
    "Разгладив складки и поправив рукой волосы, я улыбнулся отражению."
    if cosplay ==True:
        show alias at left
        m "Ты неотразим"
        hide alias
    else:
        show alias at left
        m "Ты неотразим"
        hide alias
    "Я стрельнул в зеркало из пальцев и сдул невидимый дым с “пистолета”. Настоящее рембо, которое покорит всех организаторов."
    "Так, все, надо бежать. Я вышел за дверь."
    hide scene_1_2_room

label scene_1_3m:
    "Само здание выглядело потрясно: стеклянные окна уходили куда-то вверх, а разнообразные цветы были высажены перед входом." 
    "Когда я зашла внутрь - меня сразу повстречали с распростертыми объятиями. Организатор лично жал руку всем тестировщикам и провожал к турникету."
    org "Здравствуйте, добро пожаловать!"
    "легкая улыбка тронула его губы." 
    org "Рад вас видеть! Распишитесь здесь, пожалуйста, вам нельзя рассказывать, что происходило внутри этих стен"
    "Он подмигнул и пропустил парня вперед." 
    "Моя очередь."
    m "Здравствуйте, меня зовут Элиас Гилберт."
    org "Здравствуйте, да, конечно, сейчас проверю."
    "Он начал выискивать меня в списке странно виляя пальцем, от чего я хихикнула." 
    "Его изучающий взгляд вернулся ко мне буквально на секунду, но сразу же продолжил читать дальше."
    org "Вам что-то показалось смешным?"
    m "Нет-нет, у меня бывает такое, многое кажется забавным, когда нервничаю." 
    m "Интересно, но мама, когда еще не знала, что родится мальчик - хотела назвать меня Алисой, видимо это сравнение и повлияло."
    org "Да, необычный факт." 
    "Мужчина неловко усмехнулся и продолжил поиски."
return