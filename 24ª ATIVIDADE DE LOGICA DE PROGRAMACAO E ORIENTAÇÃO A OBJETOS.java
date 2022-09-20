package br.com.teste.contas;
public class Banco {
        public String nome;
}

package br.com.teste.contas;
class Cliente {
        String nome;
        String endereco;
}

package br.com.teste.contas.main;
import br.com.teste.contas.Banco;
public class TesteBanco{
    public static void main (String[] args) {
            Banco usuarioBanco = new Banco();
            usuarioBanco.nome = "Caixa";
        
    }
}

