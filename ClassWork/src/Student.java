import com.sun.xml.internal.ws.api.ha.StickyFeature;

public class Student {
    String name;
    int roll;
    String course;
    String email;
    String grade;
    long phone;

    public static void main(String[] args) {

        Student st1 = new Student();

        print("Arish", 2, "QA", "arish@gmail.com", "A", 2408796290L);

    }
    public static void print (String name, int roll, String course, String email, String grade, long phone){
        System.out.println("Name:" + name);
        System.out.println("Roll NO: " + roll);
        System.out.println("Course Name: " +course);
        System.out.println("Email: " +email);
        System.out.println("Grade: " +grade);
        System.out.println("Phone No:" +phone);
    }
}
