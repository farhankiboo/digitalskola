
public class Main {
    public static void main(String[] args) {
        
        Academician academician2 = new Academician();
        academician2.name = "Farhan Ferdianto";
        academician2.age = "32";

        // Academician academician2 = new Academician("Farhan Ferdianto", "32");
        System.out.println(academician2.name);
        System.out.println(academician2.age);

        academician2.studentSubject("Matematika");
        
        academician2.studentSubject(null);

        Student student = new Student("Farhan Ferdianto", "32");
        student.name = "Farhan Ferdianto";
        student.age = "32";
        student.studentSubject("Farhan Ferdianto");

        // Rectangle rectangle = new Rectangle();
        // System.out.println(rectangle.getCorner());
        // System.out.println(rectangle.getParentCorner());

    }
}
// public class Main {

//     public static void main(String[] args){

//         Academician academician = new Academician();

//         // Call object
//         Academician academician = new Academician();
//         academician.name = "Farhan Ferdianto";
//         academician.age = "32";

//         // Call constructor
//         System.out.println(academician.name);
//         System.out.println(academician.age);

//         // Student.studentSubject("Farhan Ferdianto");
        
//         // Academician academician = new Academician("Farhan Ferdianto", "32");
        
//         // Student student = new Student(name: "Farhan Ferdianto");
//         // student.name = "Farhan Ferdianto";


//         // Rectangle rectangle = new Rectangle();
//         // System.out.println(rectangle.getCorner());
//         // System.out.println(rectangle.getParentCorner());
//     }

// }