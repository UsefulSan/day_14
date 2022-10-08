from storage import *


def get_info_about_products(store, shop) -> None:
    """
    Выводит информацию о количестве товаров.
    """
    print("В складе хранится:")
    for k, v in store.items.items():
        print(f"{v} шт. - {k}")
    print("\nВ магазине хранится:")
    for k, v in shop.items.items():
        print(f"{v} шт. - {k}")


def main():
    stor_items = {"печеньки": 7, "собачки": 2, "коробки": 5}
    shop_items = {"печеньки": 3, "коробки": 5}

    store = Store(stor_items)
    shop = Shop(shop_items)

    print("-" * 10 + "Информация о количестве товара" + "-" * 10)
    get_info_about_products(store, shop)
    while True:
        product_user = input("Выберите товар который хотите переместить из "
                             "склада в магазин:\n>>> ")
        amount_user = int(input("Введите количество товара:\n>>> "))
        request = Request("склад", "магазин", amount_user, product_user)

        print(request)
        print("-" * 50)

        if request.product in store.items:  # есть ли товар на складе
            if store.remove(product_user, amount_user):  # уменьшение на складе при достаточном количестве
                if shop.add(product_user, amount_user):  # добавление если есть место в магазине
                    print(f"Курьер забрал {amount_user} {product_user}"
                          f" со склада")
                    print(f"Курьер везет {amount_user} {product_user}"
                          f" со склада в магазин")
                    print(f"Курьер доставил {amount_user} {product_user} "
                          f"в магазин\n")
                    break
                else:
                    print("В магазин недостаточно места, попробуйте что то другое\n")
                    continue
            else:
                print("Не хватает на складе, попробуйте заказать меньше\n")
                continue
        else:
            print("Такого товара нет на складе. Попробуйте что-то ещё\n")
            continue

    print("-" * 10 + "Информация о количестве товара после перемещения" + "-" * 10)
    get_info_about_products(store, shop)


if __name__ == '__main__':
    main()
