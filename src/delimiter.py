from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        
        current_text = old_node.text
        current_result = []
        
        while True:
            
            opening_index = current_text.find(delimiter)
            if opening_index == -1:
                
                if current_text:
                    current_result.append(TextNode(current_text, TextType.TEXT))
                break
            
            
            if opening_index > 0:
                current_result.append(TextNode(current_text[:opening_index], TextType.TEXT))
            
            
            remaining_text = current_text[opening_index + len(delimiter):]
            closing_index = remaining_text.find(delimiter)
            
            if closing_index == -1:
                
                current_result.append(TextNode(current_text[opening_index:], TextType.TEXT))
                break
            
            
            content = remaining_text[:closing_index]
        
            current_result.append(TextNode(content, text_type))
            
            
            current_text = remaining_text[closing_index + len(delimiter):]
            
            
            if not current_text:
                break
        
        result.extend(current_result)
    
    return result