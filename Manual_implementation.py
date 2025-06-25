def manual_sort_dicts(data, key):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][key] > data[j][key]:
                data[i], data[j] = data[j], data[i]
    return data

#The AI-suggested solution using sorted() with a lambda function is more efficient, 
# readable, and pythonic. It leverages Python’s built-in Timsort algorithm, 
# which has a time complexity of O(n log n), 
# making it suitable for production use. Additionally, this version is concise—requiring only one line of logic—reducing the likelihood of bugs and enhancing maintainability.
#In contrast, the manual implementation uses a basic nested loop (similar to bubble sort), which has a time complexity of O(n²). While it is educational for understanding sorting logic,
# it is inefficient for large datasets. Furthermore, manually handling the swap logic increases the risk of subtle bugs and is not recommended when reliable alternatives exist.
#The AI-generated code demonstrates how AI tools like GitHub Copilot can quickly produce high-quality boilerplate logic, letting developers focus on more complex, high-value tasks. However, 
# developers should still verify the correctness and performance implications of AI suggestions.
#Conclusion: The AI-generated version is superior due to better performance, code simplicity, and reliability. Manual sorting is only valuable in academic or constrained environments.
