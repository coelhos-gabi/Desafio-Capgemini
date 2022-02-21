def main():
    try:
        n = int(input('Entrada: '))
        for i in range(1,n+1):
            print('*' * i)
    except:
        print('Entrada inválida')
        main()

if __name__ == '__main__':
    main()