document.addEventListener("DOMContentLoaded", () => {

  // --- CADASTRO ---
  const btnCriarConta = document.querySelector(".criarContaC");
  if (btnCriarConta) {
    btnCriarConta.addEventListener("click", () => {
      const email = document.querySelector("input[placeholder='Email']").value;
      const senha = document.querySelector("input[placeholder='Senha']").value;
      const confirma = document.querySelector("input[placeholder='Confirme Senha']").value;
      const nome = document.querySelector("input[placeholder='Nome']").value;

      if (!email || !senha || !confirma || !nome) {
        alert("Por favor, preencha todos os campos.");
        return;
      }

      if (senha !== confirma) {
        alert("As senhas não coincidem.");
        return;
      }

      // Simula salvar o usuário
      const usuario = { email, senha, nome };
      localStorage.setItem("usuario", JSON.stringify(usuario));
      alert("Conta criada com sucesso!");
      window.location.href = "login.html";
    });
  }

  // --- LOGIN ---
  const btnLogin = document.querySelector(".entrar");
  if (btnLogin) {
    btnLogin.addEventListener("click", () => {
      const email = document.querySelector("input[placeholder='Email']").value;
      const senha = document.querySelector("input[placeholder='Senha']").value;

      const usuarioSalvo = JSON.parse(localStorage.getItem("usuario"));
      if (!usuarioSalvo) {
        alert("Nenhum usuário cadastrado.");
        return;
      }

      if (email === usuarioSalvo.email && senha === usuarioSalvo.senha) {
        alert("Login realizado com sucesso!");
        // Redirecionar para a página principal
        window.location.href = "index.html";
      } else {
        alert("Email ou senha incorretos.");
      }
    });
  }

  // --- EXIBIR/ESCONDER SENHA ---
  document.querySelectorAll("input[type='password']").forEach(input => {
    const toggle = document.createElement("span");
    toggle.textContent = "👁️";
    toggle.style.cursor = "pointer";
    toggle.style.marginLeft = "10px";

    input.parentNode.insertBefore(toggle, input.nextSibling);

    toggle.addEventListener("click", () => {
      input.type = input.type === "password" ? "text" : "password";
    });
  });

  

  // --- BOTÃO VOLTAR AO TOPO ---
  const botaoTopo = document.createElement("button");
  botaoTopo.textContent = "⬆️ Topo";
  botaoTopo.style.position = "fixed";
  botaoTopo.style.bottom = "20px";
  botaoTopo.style.right = "20px";
  botaoTopo.style.padding = "10px";
  botaoTopo.style.borderRadius = "50%";
  botaoTopo.style.border = "none";
  botaoTopo.style.background = "#2280EF";
  botaoTopo.style.color = "#fff";
  botaoTopo.style.cursor = "pointer";
  botaoTopo.style.display = "none";
  botaoTopo.style.zIndex = "1000";

  document.body.appendChild(botaoTopo);

  window.addEventListener("scroll", () => {
    botaoTopo.style.display = window.scrollY > 300 ? "block" : "none";
  });

  botaoTopo.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});



const imagens = [ "imagens/Virtualthreads (2).png", "imagens/Virtualthreads (3).png"];
let index = 0;

function showImage() {
  document.getElementById('carousel-image').src = imagens[index];
}

function nextImage() {
  index = (index + 1) % imagens.length;
  showImage();
}

function prevImage() {
  index = (index - 1 + imagens.length) % imagens.length;
  showImage();
}

 // --- PARTE DE ACOMPANHAMENTO ---
const etapas = [
  { titulo: "Pedido Recebido", horario: "02/06/2025 10:21", status: "completed", icone: "fa-check" },
  { titulo: "Em Separação", horario: "02/06/2025 11:00", status: "completed", icone: "fa-check" },
  { titulo: "Em Transporte", horario: "02/06/2025 14:15", status: "current", icone: "fa-truck" },
  { titulo: "Saiu para Entrega", horario: "--/--", status: "", icone: "fa-box" },
  { titulo: "Entregue", horario: "--/--", status: "", icone: "fa-home" },
];

const container = document.getElementById("tracking");

etapas.forEach(etapa => {
  const div = document.createElement("div");
  div.className = `step ${etapa.status}`;

  div.innerHTML = `
    <div class="step-icon"><i class="fas ${etapa.icone}"></i></div>
    <div class="step-content">
      <div class="step-title">${etapa.titulo}</div>
      <div class="step-time">${etapa.horario}</div>
    </div>
  `;
  container.appendChild(div);
});
