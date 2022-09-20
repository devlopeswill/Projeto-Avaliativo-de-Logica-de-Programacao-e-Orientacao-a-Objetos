import java.io.*;
 
class Paçoca implements Serializable{}
class SerializePaçoca{
     public static void main(String args[]){
   Paçoca p = new Paçoca(); 
    
  try{
FileOutputStream fo = new FileOutputStream("test.ser");
ObjectOutputStream oo = new ObjectOutputStream(fo);
   oo.writeObject(p);
    oo.close();
System.out.println("Class Paçoca Serializado");  }
  catch(Exception e){e.printStackTrace();}         
 
 try{
    FileInputStream fi = new FileInputStream("test.ser");
    ObjectInputStream oi = new ObjectInputStream(fi);
    p =(Paçoca) oi.readObject();
    oi.close();
System.out.println("desserializado");
 }catch(Exception e){e.printStackTrace();}          }}