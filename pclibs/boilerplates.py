JAVA_BOILERPLATE = """
import java.util.Scanner;

/********************************************************************
* Autor: $author$
* Inicio: $beginning$
* Ultima alteracao: data da ultima alteração realizada no código
* Nome: $software_name$
* Funcao: $description$
********************************************************************/

public class Principal {
  public static void main(String[] args) {
    // LEMBREM-SE DE SEMPRE COMENTAR TUDO!!
    // Professor marlos aprova
    
    
    int idade; // declaracao da variavel idade
    idade = obterNumeroDeUsuario("Digite sua idade: "); // obtem idade
    
    if (idade < 18) { // se tiver menos que 18 anos
      System.out.println("oh que bonitinho!");
    } else { // caso tiver pelo menos 18 anos
      System.out.println("Veiao hein mlk kkkk");
    } // fim do if da idade
    
    System.exit(0); // sai com código 0
  } // fim da classe main
  
  public static int obterNumeroDeUsuario(String mensagem) {
    /***********************************************************
    * Metodo getIdade: pede um numero para usuario
    * Parametros:
    *     mensagem=texto em string que vai mostrar para
                   pedir dado do usuario
    * Retorno: retorna o inteiro pedido
    */
    
    Scanner input = new Scanner(System.in);
    
    int numero;
    System.out.print(mensagem);
    numero = input.nextInt();
    
    return numero;
  } // fim da função getIdade
} // fim da classe principal"""

README_TXT = """
Execute o programa a partir do arquivo "pc.exe", dentro da pasta src
"""

JAVAFX_BOILERPLATE = """/********************************************************************
* Autor: $author$
* Inicio: $beginning$
* Ultima alteracao: data da ultima alteração realizada no código
* Nome: $software_name$
* Funcao: $description$
********************************************************************/

import java.io.IOException;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import controller.MainController;

public class Principal extends Application { // A classe principal deve ser subclasse de Application
  public static void main(String[] args) {
    // LEMBREM-SE DE SEMPRE COMENTAR TUDO!!
    // Professor marlos aprova

    launch(args); // Para iniciar o programa é necessário chamar a função launch da classe Application
  } // fim da função main
  
  @Override
  public void start(Stage primaryStage) throws IOException {
    /***********************************************************
    * Metodo start: recebe um Stage (dado pelo próprio javafx)
    * Parametros:
    *     primaryStage=Stage dado pelo próprio JavaFX
    * Retorno:
    *     void
    * Erro:
    *     Como ao carregar o arquivo FXML pode retornar o erro IOException, é necessário adicionar Throw IOException
    ************************************************************/

    FXMLLoader loader = new FXMLLoader(getClass().getResource("/view/main_view.fxml")); // Cria loader do FXML
    Parent root = loader.load(); // carrega o arquivo fxml
    
    root.getStylesheets().add( "/assets/styles/main_style.css" );
    
    Scene scene = new Scene(root);
    
    primaryStage.setScene(scene);
    primaryStage.show(); // mostra o programa
  } // fim da funcao
}"""

MAIN_VIEW_BOILERPLATE = """<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.image.Image?>
<?import javafx.scene.image.ImageView?>
<?import javafx.scene.layout.AnchorPane?>
<?import javafx.scene.text.Font?>

<AnchorPane maxHeight="-Infinity" maxWidth="-Infinity" minHeight="-Infinity" minWidth="-Infinity" prefHeight="400.0" prefWidth="600.0" xmlns="http://javafx.com/javafx/11.0.1" xmlns:fx="http://javafx.com/fxml/1" fx:controller="controller.MainController">
   <children>
      <Label fx:id="clickedNumberLabel" layoutX="170.0" layoutY="153.0" text="O botao foi clicado 0 veze(s)" textAlignment="CENTER">
         <font>
            <Font name="System Bold" size="18.0" />
         </font>
      </Label>
      <Button layoutX="242.0" layoutY="200.0" mnemonicParsing="false" onAction="#updateClickCount" text="Clique em mim" />
      <ImageView fitHeight="150.0" fitWidth="200.0" pickOnBounds="true" preserveRatio="true">
         <image>
            <Image url="@../assets/images/corner.png" />
         </image>
      </ImageView>
   </children>
</AnchorPane>
"""

MAIN_CONTROLLER_BOILERPLATE = """package controller;

import javafx.fxml.FXML;
import javafx.event.ActionEvent;
import javafx.scene.control.Label;

public class MainController {
  @FXML
  public Label clickedNumberLabel;

  private int clickCount = 0;

  public void updateClickCount(ActionEvent evt) {
    clickedNumberLabel.setText("O botao foi clicado " + ++clickCount + " veze(s)");
  }
}"""

MAIN_STYLE_BOILERPLATE = """.button {
    -fx-background-color: #2700B3;
    -fx-text-fill: #e5e5e5;
    -fx-padding: 10;
}

.button:pressed {
    -fx-background-color: #6200ee;
}"""

CORNER_IMAGE = "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"