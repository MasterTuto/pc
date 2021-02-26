JAVA_BOILERPLATE = """package $package$;

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

package $package$;

import java.io.IOException;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

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

    FXMLLoader loader = new FXMLLoader(getClass().getResource("/com/$package_without_com$/view/main_view.fxml")); // Cria loader do FXML
    Parent root = loader.load(); // carrega o arquivo fxml
    
    Scene scene = new Scene(root);
    
    primaryStage.setScene(scene);
    primaryStage.show(); // mostra o programa
  } // fim da funcao
}"""

MAIN_VIEW_BOILERPLATE = """<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.scene.control.Label?>
<?import javafx.scene.layout.AnchorPane?>
<?import javafx.scene.text.Font?>


<AnchorPane maxHeight="-Infinity" maxWidth="-Infinity" minHeight="-Infinity" minWidth="-Infinity" prefHeight="400.0" prefWidth="600.0" xmlns="http://javafx.com/javafx/11.0.1" xmlns:fx="http://javafx.com/fxml/1">
   <children>
      <Label layoutX="245.0" layoutY="180.0" text="Hello, world!" textAlignment="CENTER">
         <font>
            <Font name="System Bold" size="18.0" />
         </font>
      </Label>
   </children>
</AnchorPane>
"""