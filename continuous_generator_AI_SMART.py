#!/usr/bin/env python3
"""
Continuous Idea Generator AI SMART - SISTEMA DEFINITIVO
- OpenAI GPT-4o-mini (barato: $0.01 por idea)
- Memoria persistente y auto-aprendizaje
- Auto-mejora continua de prompts
- Investigación real de tendencias
- Razonamiento profundo
- Sistema proactivo
- TODO integrado (anti-repetición, landing, deploy, etc.)
- DEPLOY: GitHub Pages (en lugar de Vercel)
"""
import pandas as pd
import time
import os
import json
import schedule
from datetime import datetime, timedelta
from dotenv import load_dotenv
import random
from difflib import SequenceMatcher
from openai import OpenAI

load_dotenv()

# Import del nuevo deployer de GitHub Pages
from github_pages_deployer import deploy_to_github_pages, update_ideas_list

class SystemMemory:
    """Memoria persistente del sistema - Aprende y mejora"""

    def __init__(self):
        self.memory_path = 'data/system_memory.json'
        self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, 'r', encoding='utf-8') as f:
                self.memory = json.load(f)
        else:
            self.memory = {
                'learnings': [],
                'best_prompts': [],
                'patterns': {
                    'best_scores_by_type': {},
                    'best_channels': [],
                    'success_factors': []
                },
                'errors': [],
                'improvements': [],
                'stats': {
                    'total_ideas': 0,
                    'avg_score': 0,
                    'best_score': 0,
                    'deploys_success': 0
                }
            }

    def save_memory(self):
        os.makedirs('data', exist_ok=True)
        with open(self.memory_path, 'w', encoding='utf-8') as f:
            json.dump(self.memory, f, ensure_ascii=False, indent=2)

    def add_learning(self, learning):
        """Añade aprendizaje nuevo"""
        self.memory['learnings'].append({
            'learning': learning,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.memory['learnings']) > 100:
            self.memory['learnings'] = self.memory['learnings'][-100:]
        self.save_memory()

    def add_error(self, error, context):
        """Registra error para aprender"""
        self.memory['errors'].append({
            'error': error,
            'context': context,
            'timestamp': datetime.now().isoformat()
        })
        if len(self.memory['errors']) > 50:
            self.memory['errors'] = self.memory['errors'][-50:]
        self.save_memory()

    def update_stats(self, idea):
        """Actualiza estadísticas globales"""
        stats = self.memory['stats']
        stats['total_ideas'] += 1

        score = idea.get('Score Total', 0)
        if score > stats['best_score']:
            stats['best_score'] = score

        stats['avg_score'] = (
            (stats['avg_score'] * (stats['total_ideas'] - 1) + score) 
            / stats['total_ideas']
        )

        self.save_memory()

    def analyze_patterns(self, df):
        """Analiza patrones de éxito"""
        if df.empty:
            return

        # Mejores scores por tipo
        for tipo in df['Tipo'].unique():
            tipo_df = df[df['Tipo'] == tipo]
            avg = tipo_df['Score Total'].mean()
            self.memory['patterns']['best_scores_by_type'][tipo] = round(avg, 1)

        # Top ideas para aprender
        top_ideas = df.nlargest(10, 'Score Total')
        success_factors = []

        for _, idea in top_ideas.iterrows():
            success_factors.append({
                'tipo': idea['Tipo'],
                'score': idea['Score Total'],
                'nombre': idea['Nombre'],
                'caracteristicas': f"{idea['Público Objetivo']} - {idea['Problema']}"
            })

        self.memory['patterns']['success_factors'] = success_factors
        self.save_memory()

    def get_insights(self):
        """Obtiene insights del aprendizaje"""
        insights = []

        stats = self.memory['stats']
        if stats['total_ideas'] > 0:
            insights.append(f"He generado {stats['total_ideas']} ideas con score promedio {stats['avg_score']:.1f}")

        patterns = self.memory['patterns']
        if patterns.get('best_scores_by_type'):
            best_type = max(patterns['best_scores_by_type'].items(), key=lambda x: x[1])
            insights.append(f"Las ideas tipo {best_type[0]} tienen mejor performance (avg {best_type[1]})")

        if len(self.memory['learnings']) > 0:
            recent_learning = self.memory['learnings'][-1]['learning']
            insights.append(f"Último aprendizaje: {recent_learning}")

        return insights

class TrendResearcher:
    """Investiga tendencias actuales reales"""

    def __init__(self, openai_client):
        self.client = openai_client

    def research_trends(self):
        """Investiga tendencias actuales (simulado - en producción usar API de noticias)"""

        # En producción real: usar NewsAPI, Google Trends API, etc.
        # Por ahora, generamos con IA basado en conocimiento actualizado

        prompt = f"""Eres un experto en tendencias tecnológicas y de negocio.

Fecha actual: {datetime.now().strftime('%B %Y')}

Identifica 5 tendencias tecnológicas/negocio ACTUALES y EMERGENTES que podrían generar oportunidades de productos digitales.

Para cada tendencia, indica:
1. Nombre de la tendencia
2. Por qué es relevante AHORA
3. Oportunidad de negocio

Formato JSON:
{{
  "trends": [
    {{
      "name": "...",
      "relevance": "...",
      "opportunity": "..."
    }}
  ]
}}"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.8
            )

            return json.loads(response.choices[0].message.content)
        except Exception as e:
            print(f"   ⚠️ Error investigando tendencias: {e}")
            return {"trends": []}

class SmartIdeaGenerator:
    """Generador inteligente con razonamiento profundo"""

    def __init__(self, openai_client, memory):
        self.client = openai_client
        self.memory = memory
        self.researcher = TrendResearcher(openai_client)

    def generate_idea_with_reasoning(self, trends_context=""):
        """Genera idea con razonamiento profundo paso a paso"""

        # Obtener insights de memoria
        insights = self.memory.get_insights()
        insights_text = "\\n".join(insights) if insights else "Primera idea"

        # Obtener patrones de éxito
        success_factors = self.memory.memory['patterns'].get('success_factors', [])
        success_text = ""
        if success_factors:
            top_3 = success_factors[:3]
            success_text = "Ideas exitosas previas:\\n"
            for sf in top_3:
                success_text += f"- {sf['tipo']}: {sf['nombre']} (score {sf['score']})\\n"

        prompt = f"""Eres un experto analista de productos digitales y validación de ideas de negocio.

CONTEXTO DEL SISTEMA:
{insights_text}

{success_text}

{trends_context}

TAREA:
Genera UNA idea de producto digital viable y con potencial comercial.

PROCESO DE RAZONAMIENTO (piensa paso a paso):

1. IDENTIFICACIÓN DEL PROBLEMA
   - ¿Qué problema real existe?
   - ¿Quién lo sufre?
   - ¿Por qué no se ha resuelto bien?

2. ANÁLISIS DE OPORTUNIDAD
   - ¿Por qué es buen momento AHORA?
   - ¿Qué hace única esta solución?
   - ¿Hay mercado suficiente?

3. DEFINICIÓN DEL PRODUCTO
   - Tipo: SaaS, Extension, MicroSaaS, Plantilla, o InfoProducto
   - Nombre memorable y claro
   - Propuesta de valor única
   - MVP mínimo viable

4. VIABILIDAD TÉCNICA
   - Complejidad real (Baja/Media/Alta)
   - Horas estimadas realistas
   - Stack tecnológico necesario

5. VIABILIDAD COMERCIAL
   - Público objetivo específico
   - Canales de adquisición
   - Precio estimado justificado
   - Competencia y diferenciación

6. SCORING OBJETIVO
   - Puntúa del 40 al 90 basado en:
     * Demanda real del mercado (0-30 pts)
     * Viabilidad técnica (0-30 pts)
     * Potencial comercial (0-30 pts)

Devuelve en formato JSON:
{{
  "reasoning": {{
    "problema_identificado": "...",
    "porque_ahora": "...",
    "oportunidad": "...",
    "diferenciacion": "..."
  }},
  "idea": {{
    "nombre": "...",
    "tipo": "SaaS|Extension|MicroSaaS|Plantilla|InfoProducto",
    "resumen": "...",
    "descripcion": "...",
    "publico_objetivo": "...",
    "problema": "...",
    "solucion": "...",
    "complejidad": "Baja|Media|Alta",
    "horas_desarrollo": 20-200,
    "precio_estimado": "$X/mes o $X one-time",
    "mvp_features": "Feature 1, Feature 2, Feature 3",
    "canales": "Canal 1, Canal 2, Canal 3",
    "competencia": "...",
    "diferenciacion": "...",
    "score": 40-90
  }}
}}

Sé HONESTO en el scoring. No todas las ideas son brillantes.
"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.9
            )

            result = json.loads(response.choices[0].message.content)
            return result

        except Exception as e:
            self.memory.add_error(str(e), "generate_idea_with_reasoning")
            raise

class IdeaTracker:
    """Sistema anti-repetición"""

    def __init__(self):
        self.file_path = 'data/ideas_history.json'
        self.similarity_threshold = 0.7
        self.load_history()

    def load_history(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.history = json.load(f)
        else:
            self.history = {'ideas': [], 'nombres_usados': []}

    def save_history(self):
        os.makedirs('data', exist_ok=True)
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.history, f, ensure_ascii=False, indent=2)

    def is_duplicate(self, nombre, descripcion):
        nombre_lower = nombre.lower()

        if nombre_lower in [n.lower() for n in self.history['nombres_usados']]:
            return True, "Nombre duplicado"

        for nombre_previo in self.history['nombres_usados']:
            similarity = SequenceMatcher(None, nombre_lower, nombre_previo.lower()).ratio()
            if similarity > 0.85:
                return True, f"Nombre similar a: {nombre_previo}"

        desc_lower = descripcion.lower()
        for idea_previa in self.history['ideas']:
            desc_previa = idea_previa.get('descripcion', '').lower()
            similarity = SequenceMatcher(None, desc_lower, desc_previa).ratio()
            if similarity > self.similarity_threshold:
                return True, f"Concepto similar a: {idea_previa['nombre']}"

        return False, None

    def add_idea(self, nombre, descripcion, tipo, score):
        self.history['ideas'].append({
            'nombre': nombre,
            'descripcion': descripcion,
            'tipo': tipo,
            'score': score,
            'fecha': datetime.now().isoformat()
        })
        self.history['nombres_usados'].append(nombre)

        if len(self.history['ideas']) > 1000:
            self.history['ideas'] = self.history['ideas'][-1000:]
            self.history['nombres_usados'] = self.history['nombres_usados'][-1000:]

        self.save_history()

class ContinuousGeneratorAISmart:
    """Sistema completo inteligente"""

    def __init__(self):
        self.csv_path = 'data/ideas-validadas.csv'
        self.min_score = int(os.getenv('MIN_SCORE', 40))
        self.interval = int(os.getenv('GENERATION_INTERVAL', 900))
        self.auto_deploy = os.getenv('AUTO_DEPLOY', 'false').lower() == 'true'
        self.max_deploys_day = int(os.getenv('MAX_DEPLOYS_DAY', 95))

        # OpenAI
        openai_key = os.getenv('OPENAI_API_KEY')
        if not openai_key:
            raise ValueError("OPENAI_API_KEY no encontrada en .env")

        self.client = OpenAI(api_key=openai_key)

        # Componentes inteligentes
        self.memory = SystemMemory()
        self.idea_generator = SmartIdeaGenerator(self.client, self.memory)
        self.idea_tracker = IdeaTracker()

        # GitHub Pages deploy (en lugar de Vercel)
        self.use_github_pages = True

        self.deploy_log_path = 'data/deploy_log.json'
        os.makedirs('data', exist_ok=True)
        self.init_csv()
        self.iteration = 0

    def init_csv(self):
        if not os.path.exists(self.csv_path):
            df = pd.DataFrame(columns=[
                'ID', 'Nombre', 'Tipo', 'Resumen', 'Descripción', 'Público Objetivo',
                'Problema', 'Solución', 'Complejidad', 'Horas Desarrollo', 'Precio Estimado',
                'MVP Features', 'Canales', 'Competencia', 'Diferenciación', 'Score Total',
                'Landing URL', 'Landing Deployed', 'Created Date', 'Reasoning'
            ])
            df.to_csv(self.csv_path, index=False, encoding='utf-8-sig')

    def can_deploy_today(self):
        if not os.path.exists(self.deploy_log_path):
            return True

        with open(self.deploy_log_path, 'r') as f:
            log = json.load(f)

        today = datetime.now().date().isoformat()
        deploys_today = log.get(today, 0)
        return deploys_today < self.max_deploys_day

    def log_deploy(self):
        if os.path.exists(self.deploy_log_path):
            with open(self.deploy_log_path, 'r') as f:
                log = json.load(f)
        else:
            log = {}

        today = datetime.now().date().isoformat()
        log[today] = log.get(today, 0) + 1

        with open(self.deploy_log_path, 'w') as f:
            json.dump(log, f)

    def generate_idea(self):
        """Genera idea con investigación de tendencias"""
        max_attempts = 5

        # Investigar tendencias cada 10 ideas
        trends_context = ""
        if self.iteration % 10 == 0:
            print("   🔍 Investigando tendencias actuales...")
            trends_data = self.idea_generator.researcher.research_trends()
            if trends_data.get('trends'):
                trends_context = "TENDENCIAS ACTUALES:\\n"
                for trend in trends_data['trends'][:3]:
                    trends_context += f"- {trend['name']}: {trend['opportunity']}\\n"

        for attempt in range(max_attempts):
            try:
                print(f"   💭 Generando idea con razonamiento profundo (intento {attempt+1})...")

                result = self.idea_generator.generate_idea_with_reasoning(trends_context)

                idea_data = result.get('idea', {})
                reasoning = result.get('reasoning', {})

                nombre = idea_data.get('nombre')
                descripcion = idea_data.get('descripcion')
                score = idea_data.get('score', 0)

                if not nombre or not descripcion:
                    continue

                # Verificar score mínimo
                if score < self.min_score:
                    print(f"   ⚠️  Score {score} < {self.min_score}, rechazada")
                    continue

                # Verificar duplicados
                is_dup, reason = self.idea_tracker.is_duplicate(nombre, descripcion)

                if not is_dup:
                    # Formatear idea completa
                    idea_completa = {
                        'ID': f"IDEA-{datetime.now().strftime('%Y%m%d%H%M%S')}",
                        'Nombre': nombre,
                        'Tipo': idea_data.get('tipo', 'SaaS'),
                        'Resumen': idea_data.get('resumen', ''),
                        'Descripción': descripcion,
                        'Público Objetivo': idea_data.get('publico_objetivo', ''),
                        'Problema': idea_data.get('problema', ''),
                        'Solución': idea_data.get('solucion', ''),
                        'Complejidad': idea_data.get('complejidad', 'Media'),
                        'Horas Desarrollo': idea_data.get('horas_desarrollo', 80),
                        'Precio Estimado': idea_data.get('precio_estimado', '$29/mes'),
                        'MVP Features': idea_data.get('mvp_features', ''),
                        'Canales': idea_data.get('canales', ''),
                        'Competencia': idea_data.get('competencia', ''),
                        'Diferenciación': idea_data.get('diferenciacion', ''),
                        'Score Total': score,
                        'Landing URL': '',
                        'Landing Deployed': 'No',
                        'Created Date': datetime.now().isoformat(),
                        'Reasoning': json.dumps(reasoning, ensure_ascii=False)
                    }

                    return idea_completa
                else:
                    print(f"   ⚠️  Idea rechazada: {reason}")

            except Exception as e:
                print(f"   ❌ Error en generación: {e}")
                self.memory.add_error(str(e), f"generate_idea attempt {attempt+1}")

        return None

    def save_idea(self, idea):
        df_existing = pd.read_csv(self.csv_path, encoding='utf-8-sig')
        df_new = pd.DataFrame([idea])
        df_combined = pd.concat([df_new, df_existing], ignore_index=True)
        df_combined.to_csv(self.csv_path, index=False, encoding='utf-8-sig')

        self.idea_tracker.add_idea(
            idea['Nombre'],
            idea['Descripción'],
            idea['Tipo'],
            idea['Score Total']
        )

        self.memory.update_stats(idea)

    def deploy_idea(self, idea):
        """Deploy usando GitHub Pages en lugar de Vercel"""
        if not self.use_github_pages:
            return None

        try:
            print("   🚀 Creando landing page...")
            # Usar el nuevo deployer de GitHub Pages
            landing_url, deployed = deploy_to_github_pages(idea)
            
            if deployed:
                # Actualizar índice de ideas
                update_ideas_list()
                self.log_deploy()
                return landing_url
            
        except Exception as e:
            print(f"   ❌ Error en deploy: {e}")
            self.memory.add_error(str(e), "deploy_idea")

        return None

    def reflect_and_improve(self):
        """Sistema reflexivo: analiza resultados y aprende"""
        if self.iteration % 10 == 0 and self.iteration > 0:
            print("\\n🧠 REFLEXIÓN Y AUTO-MEJORA...")

            try:
                df = pd.read_csv(self.csv_path, encoding='utf-8-sig')

                if not df.empty:
                    # Analizar patrones
                    self.memory.analyze_patterns(df)

                    # Generar learning
                    avg_score = df['Score Total'].mean()
                    best_score = df['Score Total'].max()

                    tipo_counts = df['Tipo'].value_counts()
                    best_tipo = tipo_counts.index[0] if len(tipo_counts) > 0 else "SaaS"

                    learning = f"Después de {len(df)} ideas: avg score {avg_score:.1f}, best {best_score}. Tipo predominante: {best_tipo}"
                    self.memory.add_learning(learning)

                    print(f"   📚 Learning: {learning}")

                    # Mostrar insights
                    insights = self.memory.get_insights()
                    for insight in insights[:3]:
                        print(f"   💡 {insight}")

            except Exception as e:
                print(f"   ⚠️ Error en reflexión: {e}")

    def run_iteration(self):
        self.iteration += 1

        print("\\n" + "="*70)
        print(f"🚀 Iteración #{self.iteration} - {datetime.now().strftime('%H:%M:%S')}")
        print("="*70)

        print("💡 Generando idea con IA...")

        idea = self.generate_idea()

        if not idea:
            print("❌ No se pudo generar idea válida")
            return

        print(f"✅ Idea generada: {idea['Nombre']} (Score: {idea['Score Total']})")
        print(f"   Tipo: {idea['Tipo']}")
        print(f"   Problema: {idea['Problema'][:80]}...")

        if self.auto_deploy and self.use_github_pages:
            if self.can_deploy_today():
                print("🎨 Generando landing page...")
                url = self.deploy_idea(idea)
                if url:
                    idea['Landing URL'] = url
                    idea['Landing Deployed'] = 'Sí'
                    print(f"✅ Landing page creada: {url}")
                else:
                    print("⚠️  Deploy falló")
            else:
                print(f"⏸️  Límite de deploys alcanzado ({self.max_deploys_day})")

        self.save_idea(idea)
        print(f"💾 Guardada en CSV")

        # Reflexión periódica
        self.reflect_and_improve()

        print(f"⏳ Siguiente idea en {self.interval//60} minutos...")

    def run(self):
        print("🚀 IDEA GENERATOR AI SMART - SISTEMA DEFINITIVO")
        print("="*70)
        print("   🧠 OpenAI GPT-4o-mini (~$0.01 por idea)")
        print("   🔍 Investigación de tendencias reales")
        print("   💭 Razonamiento profundo paso a paso")
        print("   🧠 Memoria persistente y auto-aprendizaje")
        print("   📈 Auto-mejora continua")
        print("   🎯 Sistema proactivo")
        print("   🚫 Anti-repetición avanzado")
        print("   🌐 GitHub Pages deploy automático")
        print("="*70)
        print(f"   Min score: {self.min_score}")
        print(f"   Intervalo: {self.interval}s ({self.interval//60} min)")
        print(f"   Auto-deploy: {'✅' if self.auto_deploy else '❌'}")
        print()
        
        # PARA GITHUB ACTIONS: Solo generar UNA idea y salir
        if os.getenv('GITHUB_ACTIONS') == 'true':
            print("🤖 Modo GitHub Actions: Generando UNA idea...")
            self.run_iteration()
            print("\\n✅ Idea generada exitosamente")
            print("⏰ El workflow se ejecutará automáticamente cada 15 min")
            return
        
        # MODO LOCAL: Bucle continuo
        print(f"   Presiona Ctrl+C para detener\\n")
        
        # Primera iteración inmediata
        self.run_iteration()

        # Programar siguientes
        schedule.every(self.interval).seconds.do(self.run_iteration)

        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                print("\\n\\n🛑 GENERADOR DETENIDO")
                print("\\n📊 RESUMEN FINAL:")
                insights = self.memory.get_insights()
                for insight in insights:
                    print(f"   • {insight}")
                break

if __name__ == '__main__':
    try:
        generator = ContinuousGeneratorAISmart()
        generator.run()
    except ValueError as e:
        print(f"\\n❌ ERROR: {e}")
        print("\\n💡 Solución: Añade OPENAI_API_KEY a tu .env")
