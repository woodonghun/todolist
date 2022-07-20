class Function():
    def update_todo(self):
        txt = open("C:/woo_project/todolist/widget/content", 'r')
        self.content = txt.read()
        self.content_list = self.content.split('\n')
        self.content_chunk = [self.content_list[i * 3:(i + 1) * 3] for i in
                                range((len(self.content_list) + 3 - 1) // 3)]
        txt.close()

    def change_content(self, i):
        self.update_todo()
        self.dates = self.content_chunk[i][2]
        self.title = self.content_chunk[i][0]
        self.contents = self.content_chunk[i][1]

    def setting(self):
        global number
        number = 0


