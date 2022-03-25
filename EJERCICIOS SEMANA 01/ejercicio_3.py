

class Repositorio:
    
    def __init__(self, archivos=[]):

        self.archivos_remotos = []
        self.archivos_locales = archivos
        #puedes agregar más atributos si lo estimas necesario ;)
        
    def git_add(self, archivos):
   

        for i in archivos:

            if len(i) != 1:
            
                if self.archivos_locales.count(i) == 0:
                    self.archivos_locales.append(i)

                else:
                    print(f'No se puede agregar {i}!')

            elif len(i) == 1:
                if self.archivos_locales.count(archivos) == 0:
                    self.archivos_locales.append(archivos)
                    break
                

        #debes completar aquí
        pass
        
    def git_commit(self, comentario):

        print(comentario)
        #debes completar aquí
        pass
    
    def git_push(self):
        for i in self.archivos_locales:
            if self.archivos_remotos.count(i) == 0:
                self.archivos_remotos.append(i)
            else:
                None
        

        print(f'{self.archivos_remotos}.')


        #debes completar aquí
        pass


if __name__ == "__main__":
    mi_repo = Repositorio(["main.py", "windows.py", "user.txt"])
    mi_repo.git_add('README.md')
    mi_repo.git_commit('Agregado el README :D')
    mi_repo.git_push()
    mi_repo.git_add(["data.json", "client.py", "user.txt"])
    mi_repo.git_commit("subiendo datos")
    mi_repo.git_push()