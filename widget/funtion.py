class Function():
    def update_todo(self, n):
        txt = open("C:/woo_project/todolist/widget/content.txt", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * n:(i + 1) * n] for i in
                                range((len(self.content_list) + n - 1) // n)]
        txt.close()

    def setting(self):
        global number
        number = 0


