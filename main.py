def main():
    while True:
        print("選択してください：")
        print("1: 佐藤")
        print("2: 大谷")
        print("3: メンバー3の名前")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("よろしく")
        elif choice == "2":
            print("こちらこそよろしく")
        elif choice == "3":
            print("メンバー3のコメント")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
