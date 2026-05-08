#include <stdio.h>
#include <string.h>

#define MAX_NOTES 3

typedef struct
{
    int id;
    char title[100];
    char content[500];
} Note;

void print_welcome(void);                      // приветствие
void fill_test_notes(Note notes[], int count); // заполнение структуры
void print_notes(Note notes[], int count);     // вывод заметок на экран
void add_note(Note notes[], int *count);       // добавление заметки
void remove_newline(char text[]); // убрать /n из строки вывода

int main(void)
{
    print_welcome();

    Note notes[MAX_NOTES];
    int count = 2;

    fill_test_notes(notes, count);
    add_note(notes, &count);
    print_notes(notes, count);
    return 0;
}

void print_welcome(void)
{
    char name[100];
    printf("Enter your name: ");
    if (fgets(name, sizeof(name), stdin) == NULL)
    {
        printf("Error reading input.\n");
        return;
    }
    printf("Hello, %s", name);
    printf("Notes Manager\n");
}

void fill_test_notes(Note notes[], int count)
{
    notes[0].id = 1;
    snprintf(notes[0].title, sizeof(notes[0].title), "Test title 1");
    snprintf(notes[0].content, sizeof(notes[0].content), "Test content 1");

    notes[1].id = 2;
    snprintf(notes[1].title, sizeof(notes[1].title), "Test title 2");
    snprintf(notes[1].content, sizeof(notes[1].content), "Test content 2");

    notes[2].id = 3;
    snprintf(notes[2].title, sizeof(notes[2].title), "Test title 3");
    snprintf(notes[2].content, sizeof(notes[2].content), "Test content 3");
}

void print_notes(Note notes[], int count)
{
    for (int i = 0; i < count; i++)
    {
        printf("\nNote %d:\n", i + 1);
        printf("ID: %d\n", notes[i].id);
        printf("Title: %s\n", notes[i].title);
        printf("Content: %s\n", notes[i].content);
    }
}

void add_note(Note notes[], int *count)
{
    if (*count >= MAX_NOTES)
    {
        printf("No space for new notes.\n");
        return;
    }

    int index = *count;
    notes[index].id = index + 1;

    printf("Enter note title: ");
    if (fgets(notes[index].title, sizeof(notes[index].title), stdin) == NULL)
    {
        printf("Error reading title.\n");
        return;
    }
    remove_newline(notes[index].title);
    printf("Enter note content: ");
    if (fgets(notes[index].content, sizeof(notes[index].content), stdin) == NULL)
    {
        printf("Error reading content.\n");
        return;
    }
    remove_newline(notes[index].content);
    (*count)++;
}

void remove_newline(char text[])
{
    size_t len = strlen(text);
    if (len > 0 && text[len - 1] == '\n')
    {
        text[len - 1] = '\0';
    }
}