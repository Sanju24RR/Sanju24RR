class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def build_huffman_tree(data):
    frequency = {}
    for char in data:
        frequency[char] = frequency.get(char, 0) + 1  
    nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)      
        left = nodes.pop(0)
        right = nodes.pop(0)      
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right      
        nodes.append(internal_node) 
    return nodes[0]

def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}  
    if node.char is not None:
        mapping[node.char] = code
        return  
    if node.left:
        build_huffman_codes(node.left, code + "0", mapping)    
    if node.right:
        build_huffman_codes(node.right, code + "1", mapping)    
    return mapping

def huffman_encode(data):
    if not data:
        return "", {}, None
    if len(data) == 1:
        return "0", {data: "0"}, HuffmanNode(data, 1)
    root = build_huffman_tree(data)
    huffman_codes = build_huffman_codes(root)
    encoded_data = ""
    for char in data:
        encoded_data += huffman_codes[char]
    return encoded_data, huffman_codes, root

def huffman_decode(encoded_data, root):
    if not root or not encoded_data:
        return ""  
    decoded_data = ""
    current = root   
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right            
        if current.char is not None:
            decoded_data += current.char
            current = root
    return decoded_data

# Example usage and testing
if __name__ == "__main__":
    # Test with a sample string
    data = "hello world"
    print(f"Original data: {data}")
    # Encode
    encoded_data, codes, tree = huffman_encode(data)
    print("\nHuffman Codes:")
    for char, code in codes.items():
        print(f"'{char}': {code}")
    print(f"\nEncoded data: {encoded_data}")
    # Decode
    decoded_data = huffman_decode(encoded_data, tree)
    print(f"Decoded data: {decoded_data}") 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     class HuffmanNode:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None

# def build_huffman_tree(data):
#     # Calculate frequency of each character
#     frequency = {}
#     for char in data:
#         frequency[char] = frequency.get(char, 0) + 1  
#     # Create initial nodes for each character
#     nodes = [HuffmanNode(char, freq) for char, freq in frequency.items()]
#     while len(nodes) > 1:
#         # Sort nodes by frequency
#         nodes.sort(key=lambda x: x.freq)      
#         # Take two nodes with lowest frequencies
#         left = nodes.pop(0)
#         right = nodes.pop(0)      
#         # Create new internal node with these two as children
#         internal_node = HuffmanNode(None, left.freq + right.freq)
#         internal_node.left = left
#         internal_node.right = right      
#         # Add the new node back to the list
#         nodes.append(internal_node) 
#     # Return root of Huffman Tree
#     return nodes[0]

# def build_huffman_codes(node, code="", mapping=None):
#     if mapping is None:
#         mapping = {}  
#     # If leaf node, store the code for this character
#     if node.char is not None:
#         mapping[node.char] = code
#         return  
#     # Traverse left (add 0 to code)
#     if node.left:
#         build_huffman_codes(node.left, code + "0", mapping)    
#     # Traverse right (add 1 to code)
#     if node.right:
#         build_huffman_codes(node.right, code + "1", mapping)    
#     return mapping

# def huffman_encode(data):
#     # Handle empty input
#     if not data:
#         return "", {}, None
#     # Handle single character input
#     if len(data) == 1:
#         return "0", {data: "0"}, HuffmanNode(data, 1)
#     # Build Huffman tree
#     root = build_huffman_tree(data)
#     # Generate Huffman codes
#     huffman_codes = build_huffman_codes(root)
#     # Encode the data
#     encoded_data = ""
#     for char in data:
#         encoded_data += huffman_codes[char]
#     return encoded_data, huffman_codes, root

# def huffman_decode(encoded_data, root):
#     if not root or not encoded_data:
#         return ""  
#     decoded_data = ""
#     current = root   
#     for bit in encoded_data:
#         # Traverse left for '0'
#         if bit == '0':
#             current = current.left
#         # Traverse right for '1'
#         else:
#             current = current.right            
#         # If leaf node, we've found a character
#         if current.char is not None:
#             decoded_data += current.char
#             current = root
#     return decoded_data

# # Example usage and testing
# if __name__ == "__main__":
#     # Test with a sample string
#     data = "hello world"
#     print(f"Original data: {data}")
#     # Encode
#     encoded_data, codes, tree = huffman_encode(data)
#     print("\nHuffman Codes:")
#     for char, code in codes.items():
#         print(f"'{char}': {code}")
#     print(f"\nEncoded data: {encoded_data}")
#     # Decode
#     decoded_data = huffman_decode(encoded_data, tree)
#     print(f"Decoded data: {decoded_data}") 
#     # # Calculate compression ratio
#     # original_bits = len(data) * 8
#     # compressed_bits = len(encoded_data)
#     # compression_ratio = (1 - compressed_bits/original_bits) * 100 
#     # print(f"\nCompression Analysis:")
#     # print(f"Original size: {original_bits} bits")
#     # print(f"Compressed size: {compressed_bits} bits")
#     # print(f"Compression ratio: {compression_ratio:.2f}%")