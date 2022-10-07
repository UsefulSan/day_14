# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных, 
# чтобы было понятно, за что эти переменные отвечают 
# и что происходит и без комментариев


class Unit:
    def movement_character(self, field, character_x, character_y, movement_direction, flying, sneaking, speed=1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param character_x: x-координата юнита
        :param character_y: у- координата юнита
        :param movement_direction: направление перемещения
        :param flying: летит ли юнит
        :param sneaking: крадется ли юнит
        :param speed: базовый параметр скорости
        """
        if flying and sneaking:
            raise ValueError('Рожденный ползать летать не должен!')
        if flying:
            speed *= 1.2
            if movement_direction == 'UP':
                new_y = character_y + speed
                new_x = character_x
            elif movement_direction == 'DOWN':
                new_y = character_y - speed
                new_x = character_x
            elif movement_direction == 'LEFT':
                new_y = character_y
                new_x = character_x - speed
            elif movement_direction == 'RIGHT':
                new_y = character_y
                new_x = character_x + speed
        if sneaking:
            speed *= 0.5
            if movement_direction == 'UP':
                new_y = character_y + speed
                new_x = character_x
            elif movement_direction == 'DOWN':
                new_y = character_y - speed
                new_x = character_x
            elif movement_direction == 'LEFT':
                new_y = character_y
                new_x = character_x - speed
            elif movement_direction == 'RIGHT':
                new_y = character_y
                new_x = character_x + speed

            field.set_unit(x=new_x, y=new_y, unit=self)
