import time

from PySide2 import QtWidgets as QW, QtGui as QG, QtCore as QC
import random

from api.note import Note, get_notes

citations = ["« Soyez vous-même tous les autres sont déjà pris » - Oscar Wilde","« J’ai raté 9 000 tirs dans ma carrière. J’ai perdu presque 300 matchs. 26 fois, on m’a fait confiance pour prendre le tir de la victoire et j’ai raté. J’ai échoué encore et encore et encore dans ma vie. Et c’est pourquoi je réussis. » – Michael Jordan","« Dans 20 ans, vous serez plus déçu par les choses que vous n’avez pas faites que par celles que vous avez faites. Alors, sortez des sentiers battus. Mettez les voiles. Explorez. Rêvez. Découvrez. » – Mark Twain","« Faites ce que vous pouvez, avec ce que vous avez, là où vous êtes. » – Theodore Roosevelt","« Toute personne qui n’a jamais commis d’erreurs n’a jamais tenté d’innover. » – Albert Einstein", "« Je connais un moyen de ne pas vieillir : c’est d’accueillir les années comme elle viennent et avec le sourire… un sourire, c’est toujours jeune. » - Pierre Dac","« Pour ce qui est de l’avenir, il ne s’agit pas de le prévoir mais de le rendre possible.» - Antoine de Saint-Exupéry","« Si vous ne voulez pas qu’on vous oublie, le jour où vous serez mort et pourri, écrivez des choses qui valent la peine d’être lues ou faites, des choses qui valent la peine d’être écrites. » – Benjamin Franklin","« Quand tout semble être contre vous, souvenez-vous que l’avion décolle face au vent, et non avec lui. » – Henry Ford","« Ne laissez personne vous voler votre imagination, votre créativité ou votre curiosité. C’est votre place dans le monde, c’est votre vie. » – Mae C. Jemison","« Laissez-vous guider par votre rêve, même si vous devez momentanément le mettre de côté pour trouver un emploi ou payer votre loyer. Et restez toujours ouvert aux opportunités de sortir du cadre pour mener la vie et faire les choses qui vous inspirent profondément… n’ayez pas peur. » - Jane Goodall","« Quand vous adorez une fleur, vous l’arrachez, mais quand vous aimez une fleur, vous l’arrosez tous les jours. Celui qui comprend ça, comprend la vie. » - Bouddha","« J’ai toujours préféré la folie des passions à la sagesse de l’indifférence » - Anatole France","« Si vous faites ce que vous avez toujours fait, vous obtiendrez ce que vous avez toujours obtenu. » – Anthony Robbins","« Trop d’entre nous ne vivent pas leurs rêves car nous vivons nos peurs. » – Les Brown","« La meilleure manière de se lancer, c’est d’arrêter de parler et commencer à agir. » – Walt Disney","« J’ai appris que les gens oublieront ce que vous avez dit, ils oublieront ce que vous avez fait, mais ils n’oublieront jamais ce que vous leur avez fait ressentir. » – Maya Angelou","« Quand j'étais petit, ma mère m'a dit que le bonheur était la clé de la vie. Quand je suis allé à l'école, ils m'ont demandé ce que je voulais être quand je serais grand. J'ai répondu heureux. Ils m'ont dit que je n'avais pas compris la question. J'ai répondu qu'ils n'avaient pas compris la vie. » - John Lennon","« Donnez à chaque jour la chance de devenir le plus beau jour de votre vie. » - Mark Twain","« Je veux rester folle, vivre ma vie comme je la rêve et non de la manière imposée par les autres. » - Paulo Coelho","« Beaucoup de chemins mènent à la réussite, mais un seul mène immanquablement à l’échec, celui qui consiste à tenter de plaire à tout le monde. » - Benjamin Franklin","« Tu ne sais pas à quel point tu es fort jusqu’au jour où être fort devient la seule option. » - Bob Marley","« Si votre champ de vision est suffisamment large, vous comprendrez que ce qui vous arrive dans le temps présent vous prépare à un plus grand futur» - Sanaya Roman","« Si vous voulez que la vie vous sourie apportez lui d’abord votre bonne humeur » - Spinoza","« Si tu veux construire un bateau, ne rassemble pas tes hommes et femmes pour leur donner des ordres, pour expliquer chaque détail, pour leur dire où trouver chaque chose… Si tu veux construire un bateau, fais naître dans le cœur de tes hommes et femmes le désir de la mer. » - Antoine de Saint-Exupéry","« 100 % des choses qu’on ne tente pas échouent. » – Wayne Gretzky","« Les grandes transformations se font à petits pas. Pose une pierre chaque jour, n’abandonne jamais ta construction, et l’édifice grandira. Combats le doute et la paresse. Tiens constamment ton esprit en éveil. Observe, comprends, et aime. » - Dugpa Rimpoché","« Se libérer de la peur, c’est le premier pas, la clef du changement. » - Antonella Verdiani ","« Le succès c’est d’aller d’échec en échec sans perdre son enthousiasme. » – Winston Churchill","« Hier n’existe plus. Demain ne viendra peut-être jamais. Il n’y a que le miracle du moment présent. Savourez-le. C’est un cadeau » - Marie Stilkind","« Souvenez-vous que ne pas obtenir ce que l’on veut peut parfois se révéler être un incroyable coup de chance. » - Tenzin Gyatzo, le 14e Dalaï Lama","« Le seul homme qui ne se trompe jamais est celui qui ne fait jamais rien. N’ayez pas peur des erreurs, pourvu que vous ne fassiez pas deux fois la même. » - Franklin Delano Roosevelt","« Laisse moi mes folies. Une petite flamme de folie, si on savait comme la vie s’en éclaire ! » - Henry de Montherlant","« J’ai décidé d’être heureux parce que c’est bon pour la santé. » – Voltaire","« Nul besoin de faire de la Terre un paradis : elle en est un. A nous de nous adapter pour l’habiter. » - Henry Miller","« Ne vous arrêtez pas à la vision limitée que vous avez de vous et de votre vie! Il y a en vous une énergie plus forte vous permettant de dépasser ce qui vous limite. » - Catherine Balance","« Rappelle-toi : l’unique personne qui t’accompagne toute la vie, c’est toi-même ! Sois vivant dans tout ce que tu fais. » - Pablo Picasso","« Les gens blâment sans cesse les circonstances pour expliquer ce qu’ils sont. Je ne crois pas aux circonstances. Les gens qui font leur chemin dans la vie sont ceux qui se lèvent le matin et qui partent à la recherche des circonstances auxquelles ils aspirent. Et s’ils ne les trouvent pas, ils les créent. » - George Bernard Shaw","« Voir le possible là où les autres voient l’impossible, telle est la clé du succès. » - Charles-Albert Poissant","« Quand tu penses à la réussite, n’en fais pas une vague rêverie, sans passion, sans force. Considère-là avec amour, cajole-là, prends soin d’elle dans tes rêves, dans ton coeur. Alors elle se rendra visible.» - Dugpa Rimpoché","« Le mental intuitif est un don sacré et le mental rationnel est un serviteur fidèle. Nous avons créé une société qui honore le serviteur et a oublié le don.» - Albert Einstein","« Ce n’est pas parce que les choses sont difficiles que nous n’osons pas les faire. C’est parce que nous n’osons pas les faire qu’elles sont difficiles » – Sénèque","« La plupart des gens passent leur vie en cherchant toujours quelque chose d’autre, ils traversent l’existence persuadés que leur objectif est fort lointain alors qu’autour d’eux se trouve tout ce dont ils ont besoin pour atteindre leur but. » -Fun-Chang","« Il y a au fond de vous de multiples petites étincelles de potentialités; elles ne demandent qu’un souffle pour s’enflammer en de magnifiques réussites. » - Wilferd A. Peterson","« Quoi que tu rêves d’entreprendre, commence-le. L’audace a du génie, du pouvoir, de la magie. » - Johann Wolfgang Von Goethe","« Gardons tous à l’esprit que nous faisons partie d’un tout, nous sommes tous reliés les uns aux autres et suivons les mêmes rythmes et les mêmes lois – les lois de la nature. Laissons-nous le champ des possibles sur ce qui nous échappe » - Julien Peron","« Le pessimisme est d’humeur; l’optimisme est de volonté. »- Emile Chartier","« Le plus grand échec que vous puissiez avoir dans la vie, c’est de ne pas essayer du tout. » - Emil Motycka","« La logique vous conduira d’un point A à un point B. L’imagination et l’audace vous conduiront où vous le désirez. »- Albert Einstein"]


class MainWindow(QW.QWidget):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__()
        self.setWindowTitle("MotivText")
        self.setup_ui()
        self.populate_notes()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.btn_createNote = QW.QPushButton("Créer une note")
        self.lw_notes = QW.QListWidget()
        self.te_contenu = QW.QTextEdit()
        self.btn_undo = QW.QPushButton()
        self.btn_redo = QW.QPushButton()
        self.ico_undo = QG.QIcon("C:/Users/cece0/OneDrive/Documents/celian/programmes/phyton/PyNotes/assets/8665020_arrow_rotate_left_icon.png")
        self.ico_redo = QG.QIcon("C:/Users/cece0/OneDrive/Documents/celian/programmes/phyton/PyNotes/assets/8665088_arrow_rotate_right_icon.png")
        self.txt_citation = QW.QLabel(random.choice(citations))
        self.timer = QC.QTimer(self)

    def modify_widgets(self):
        self.btn_redo.setIcon(self.ico_redo)
        self.btn_undo.setIcon(self.ico_undo)
        self.te_contenu.setUndoRedoEnabled(True)
        self.te_contenu.setPlaceholderText("Ecrivez ici votre note")
        self.txt_citation.setAlignment(QC.Qt.AlignCenter)
        self.txt_citation.setWordWrap(True)
        css_file = self.ctx.get_resource("style.css")
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

    def create_layouts(self):
        self.main_layout = QW.QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.btn_createNote,2,0,1,1)
        self.main_layout.addWidget(self.lw_notes,3,0,1,1)
        self.main_layout.addWidget(self.te_contenu,3,1,2,2)
        self.main_layout.addWidget(self.btn_undo, 2,1,1,1)
        self.main_layout.addWidget(self.btn_redo, 2,2,1,1)
        self.main_layout.addWidget(self.txt_citation, 0,0,2,3)
    def setup_connections(self):
        self.btn_createNote.clicked.connect(self.create_notes)
        self.te_contenu.textChanged.connect(self.save_note)
        self.lw_notes.itemSelectionChanged.connect(self.populate_notes_content)
        QW.QShortcut(QG.QKeySequence("Delete"), self.lw_notes, self.delete_selected_note)
        self.btn_undo.clicked.connect(self.te_contenu.undo)
        self.btn_redo.clicked.connect(self.te_contenu.redo)
        self.timer.timeout.connect(self.changement_de_citation)
        self.timer.start(15000)

    def add_note_to_listwidget(self,note):
        lw_item = QW.QListWidgetItem(note.title)
        lw_item.note = note
        self.lw_notes.addItem(lw_item)

    def create_notes(self):
        title, result = QW.QInputDialog.getText(self, "Ajouter une note", "Titre: ")
        if title and result:
            note = Note(title)
            note.save()
            self.add_note_to_listwidget(note)
    def delete_selected_note(self):
        selected_item = self.get_selected_lw_item()
        if selected_item:
            resultat = selected_item.note.delete()
            if resultat:
                self.lw_notes.takeItem(self.lw_notes.row(selected_item))

    def get_selected_lw_item(self):
        selected_items = self.lw_notes.selectedItems()
        if selected_items:
            return selected_items[0]
        else:
            return None

    def populate_notes(self):
        notes = get_notes()
        for note in notes:
            self.add_note_to_listwidget(note)

    def populate_notes_content(self):
        selected_item = self.get_selected_lw_item()
        if selected_item:
            self.te_contenu.setText(selected_item.note.content)
        else:
            self.te_contenu.clear()

    def save_note(self):
        selected_item = self.get_selected_lw_item()
        if selected_item:
            selected_item.note.content = self.te_contenu.toPlainText()
            selected_item.note.save()

    def changement_de_citation(self):
        prochaine_citation = random.choice(citations)
        animation = QC.QPropertyAnimation(self.txt_citation, b"opacity")
        animation.setDuration(100)
        animation.setStartValue(1.0)
        animation.setEndValue(0.0)
        animation.start()
        time.sleep(1.0)
        self.txt_citation.setText(prochaine_citation)
        self.timer.start(15000)