#!/usr/bin/env python3
"""
GitHub Pages Deployer
Crea landing pages estáticas y las guarda en carpeta landing-pages/
"""
import os
import json
from datetime import datetime

def deploy_to_github_pages(idea_data):
    """
    Crea landing page HTML y la guarda en carpeta landing-pages/
    """
    try:
        # Crear carpeta si no existe
        os.makedirs('landing-pages', exist_ok=True)
        
        # Crear nombre de archivo único
        idea_id = idea_data.get('ID', 'unknown')
        filename = f"landing-pages/{idea_id}.html"
        
        # Sanitizar texto para HTML (escapar caracteres especiales)
        def clean(text):
            if not text:
                return ""
            text = str(text)
            text = text.replace('&', '&amp;')
            text = text.replace('<', '&lt;')
            text = text.replace('>', '&gt;')
            text = text.replace('"', '&quot;')
            text = text.replace("'", '&#39;')
            return text
        
        nombre = clean(idea_data.get('Nombre', 'Idea'))
        score = idea_data.get('Score Total', 0)
        tipo = clean(idea_data.get('Tipo', 'Digital'))
        resumen = clean(idea_data.get('Resumen', ''))
        descripcion = clean(idea_data.get('Descripción', ''))
        publico = clean(idea_data.get('Público Objetivo', ''))
        problema = clean(idea_data.get('Problema', ''))
        solucion = clean(idea_data.get('Solución', ''))
        mvp = clean(idea_data.get('MVP Features', ''))
        complejidad = clean(idea_data.get('Complejidad', 'Media'))
        horas = clean(idea_data.get('Horas Desarrollo', '80'))
        precio = clean(idea_data.get('Precio Estimado', '$29/mes'))
        canales = clean(idea_data.get('Canales', ''))
        competencia = clean(idea_data.get('Competencia', ''))
        diferenciacion = clean(idea_data.get('Diferenciación', ''))
        fecha = clean(idea_data.get('Created Date', datetime.now().strftime('%Y-%m-%d %H:%M')))
        
        # Procesar MVP features como lista
        mvp_items = ''
        if mvp:
            features = mvp.split(',')
            for feature in features:
                if feature.strip():
                    mvp_items += f'<li>{clean(feature.strip())}</li>'
        
        # Generar HTML limpio
        html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{nombre} - Idea Validator AI</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,sans-serif;line-height:1.6;color:#1a1a1a;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);min-height:100vh;padding:40px 20px}}
.container{{max-width:900px;margin:0 auto;background:#fff;border-radius:20px;padding:50px;box-shadow:0 20px 60px rgba(0,0,0,0.3)}}
h1{{color:#667eea;font-size:3em;margin-bottom:20px}}
.score{{background:linear-gradient(135deg,#10b981,#059669);color:#fff;padding:15px 30px;border-radius:50px;display:inline-block;font-size:1.5em;font-weight:700;margin:20px 0}}
.tag{{background:#667eea;color:#fff;padding:8px 20px;border-radius:20px;display:inline-block;margin:5px;font-size:0.9em}}
.section{{margin:30px 0;padding:25px;background:#f9fafb;border-radius:12px;border-left:4px solid #667eea}}
.section h2{{color:#374151;margin-bottom:15px;font-size:1.4em}}
.section p{{color:#4b5563;line-height:1.8}}
.info-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:15px;margin-top:15px}}
.info-card{{background:#fff;padding:15px;border-radius:8px;border:1px solid #e5e7eb}}
.info-card strong{{color:#667eea;display:block;margin-bottom:5px}}
ul{{margin-left:20px;margin-top:10px}}
li{{margin:8px 0;color:#4b5563}}
.footer{{text-align:center;margin-top:50px;padding-top:30px;border-top:2px solid #e5e7eb;color:#6b7280}}
.footer a{{color:#667eea;text-decoration:none;font-weight:600}}
</style>
</head>
<body>
<div class="container">
<h1>🚀 {nombre}</h1>
<div>
<span class="score">📊 Score: {score}/100</span>
<span class="tag">{tipo}</span>
</div>
<div class="section">
<h2>📋 Resumen Ejecutivo</h2>
<p>{resumen}</p>
</div>
<div class="section">
<h2>📖 Descripción Detallada</h2>
<p>{descripcion}</p>
</div>
<div class="section">
<h2>🎯 Público Objetivo</h2>
<p>{publico}</p>
</div>
<div class="section">
<h2>❌ Problema que Resuelve</h2>
<p>{problema}</p>
</div>
<div class="section">
<h2>✅ Solución Propuesta</h2>
<p>{solucion}</p>
</div>
<div class="section">
<h2>⚙️ Características MVP</h2>
<ul>{mvp_items}</ul>
</div>
<div class="section">
<h2>📊 Información Técnica y Financiera</h2>
<div class="info-grid">
<div class="info-card"><strong>Complejidad</strong>{complejidad}</div>
<div class="info-card"><strong>Horas de Desarrollo</strong>{horas}</div>
<div class="info-card"><strong>Precio Estimado</strong>{precio}</div>
</div>
</div>
<div class="section">
<h2>🎯 Canales de Distribución</h2>
<p>{canales}</p>
</div>
<div class="section">
<h2>🏆 Análisis Competitivo</h2>
<p><strong>Competencia:</strong> {competencia}</p>
<p style="margin-top:15px"><strong>Diferenciación:</strong> {diferenciacion}</p>
</div>
<div class="footer">
<p>✨ Idea generada automáticamente por <strong>Idea Validator AI</strong></p>
<p>🤖 Powered by OpenAI GPT-4o-mini</p>
<p>📅 Creada el {fecha}</p>
<p style="margin-top:15px"><a href="index.html">← Volver al listado de ideas</a></p>
</div>
</div>
</body>
</html>"""
        
        # Guardar archivo HTML
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            f.write(html_content)
        
        # URL relativa para GitHub Pages
        landing_url = f"{idea_id}.html"
        
        print(f"✅ Landing page creada: {filename}")
        return landing_url, True
        
    except Exception as e:
        print(f"❌ Error creando landing page: {str(e)}")
        import traceback
        traceback.print_exc()
        return "", False


def update_ideas_list():
    """
    Lee todas las ideas del CSV y genera el archivo ideas-list.json
    para el índice de GitHub Pages
    """
    try:
        import pandas as pd
        
        csv_path = 'data/ideas-validadas.csv'
        
        if not os.path.exists(csv_path):
            print("⚠️  CSV no encontrado")
            return
        
        # Leer CSV
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        
        # Convertir a lista de diccionarios
        ideas_list = []
        
        for _, row in df.iterrows():
            idea = {
                'id': str(row.get('ID', '')),
                'nombre': str(row.get('Nombre', '')),
                'tipo': str(row.get('Tipo', '')),
                'resumen': str(row.get('Resumen', ''))[:150] + '...',
                'score': int(row.get('Score Total', 0)),
                'landing_url': str(row.get('Landing URL', ''))
            }
            ideas_list.append(idea)
        
        # Ordenar por score descendente
        ideas_list.sort(key=lambda x: x['score'], reverse=True)
        
        # Guardar JSON
        json_path = 'landing-pages/ideas-list.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(ideas_list, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Lista de ideas actualizada: {len(ideas_list)} ideas")
        
    except Exception as e:
        print(f"❌ Error actualizando lista de ideas: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    # Test
    test_idea = {
        'ID': 'test-001',
        'Nombre': 'Test Idea',
        'Tipo': 'SaaS',
        'Resumen': 'Una idea de prueba',
        'Descripción': 'Descripción completa de la idea de prueba',
        'Público Objetivo': 'Desarrolladores',
        'Problema': 'Problema de prueba',
        'Solución': 'Solución de prueba',
        'MVP Features': 'Feature 1, Feature 2, Feature 3',
        'Complejidad': 'Media',
        'Horas Desarrollo': 80,
        'Precio Estimado': '$29/mes',
        'Canales': 'SEO, Social Media',
        'Competencia': 'Competidor X',
        'Diferenciación': 'Diferenciador Y',
        'Score Total': 75,
        'Created Date': datetime.now().isoformat()
    }
    
    url, success = deploy_to_github_pages(test_idea)
    
    if success:
        print(f"✅ Test exitoso: {url}")
    else:
        print("❌ Test falló")
