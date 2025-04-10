#include <iostream>
using namespace std;

// Forward declaration
class Circle;
class Rectangle;

// Giao diện Visitor: khai báo các phương thức visit cho từng loại đối tượng
class Visitor
{
public:
    virtual void visit(Circle *c) = 0;
    virtual void visit(Rectangle *r) = 0;
};

// Giao diện Element (Shape): khai báo phương thức accept để chấp nhận Visitor
class Shape
{
public:
    virtual void accept(Visitor *visitor) = 0;
};

// Lớp Circle kế thừa từ Shape
class Circle : public Shape
{
public:
    void accept(Visitor *visitor) override
    {
        // Khi chấp nhận visitor, gọi phương thức visit dành cho Circle
        visitor->visit(this);
    }
    void draw()
    {
        cout << "Drawing Circle" << endl;
    }
};

// Lớp Rectangle kế thừa từ Shape
class Rectangle : public Shape
{
public:
    void accept(Visitor *visitor) override
    {
        // Khi chấp nhận visitor, gọi phương thức visit dành cho Rectangle
        visitor->visit(this);
    }
    void draw()
    {
        cout << "Drawing Rectangle" << endl;
    }
};

// Visitor cụ thể: PrintVisitor, thực hiện hành động in ra màn hình
class PrintVisitor : public Visitor
{
public:
    void visit(Circle *c) override
    {
        cout << "Visiting a Circle: ";
        c->draw();
    }
    void visit(Rectangle *r) override
    {
        cout << "Visiting a Rectangle: ";
        r->draw();
    }
};

int main()
{
    // Tạo mảng các đối tượng Shape
    Shape *shapes[] = {new Circle(), new Rectangle()};

    // Tạo một visitor cụ thể
    PrintVisitor pv;

    // Duyệt qua các đối tượng và gọi phương thức accept của từng đối tượng
    for (Shape *shape : shapes)
    {
        shape->accept(&pv);
    }

    // Giải phóng bộ nhớ đã cấp phát
    for (Shape *shape : shapes)
    {
        delete shape;
    }

    return 0;
}
