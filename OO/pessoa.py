class Pessoa:
    def cumprimentar(self):
        return 'Ola'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
