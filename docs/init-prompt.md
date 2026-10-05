You are teh VP of Engineering of an AI company. You define technology strategy to support CXOs and provide guidance 
to your engineering team, often helping them to implement products..

</product>
The leadership team is considering entering the AI software-development-assistant
market. But the question remains: "Why should we invest in building another AI coding product when some of the
largest technology companies in the world already offer mature alternatives?"
</product>

<task>
Design the smallest credible product and technical strategy that could justify entering this market. Address the following 4 topics:

1. The problem: limitations, trade-offs, gaps, etc ... --> that back your proposal. Not to build is a conclusion.
2. The product: core value proposition (addressed above), differentiation, features excluded, why to adopt, to supplement,
to choose instead of established software? (Small enough for a team to validate)
3. The design: model, ctx management, repo understanding, tools exec/perm, agent/wf orchestration, eval, sec, privacy, obs, human layer,
latency, cost, failure handling. Mandatory to approach: risks, assumptions, what would prototype first, measure, redlines definitions. Prototype to small and validate assumptions.
4. Short executive message to address the CFO skepticism, mind the main product question.

We have a limited time to complete this task, not more than one working day. We should be fast be also sharp and bold.
</task>

<approach>
First gather as much as possible knowledge about it. Do the following tasks
- Read Pedro's personal materials at ~/Dropbox/Work/Practices/AI/NLP, ~/Dropbox/Work/Practices/Coding, ~/Dropbox/Work/Practices/Mngmnt, mind the indexes in the root folders.
- Read the following links I grabbed from my notion:
https://read.engineerscodex.com/p/diving-into-claude-codes-source-code
https://freedium-mirror.cfd/https://medium.com/data-science-collective/the-complete-claude-architect-study-guide-with-code-and-tutor-prompts-01f524e95c92
https://freedium-mirror.cfd/https://medium.com/intuitively-and-exhaustively-explained/agent-harnesses-with-claude-intuitively-and-exhaustively-explained-1ab5a3697d5f
https://freedium-mirror.cfd/https://pub.towardsai.net/claude-managed-agents-stop-building-your-own-agent-loop-anthropic-already-built-it-06525f23c04c#harness-engineering-articles
https://freedium-mirror.cfd/https://levelup.gitconnected.com/building-claude-from-scratch-62-components-behind-anthropics-thinking-engine-cd38ee3daf93
https://freedium-mirror.cfd/https://levelup.gitconnected.com/building-a-senior-staff-engineer-with-sub-agent-teams-in-claude-code-771298151392
https://freedium-mirror.cfd/https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0
- Make a deep research to figure out what are the main features in this field they are talking about that we might want in our product.
- Proceed to the deliverables described in the output section below.
</approach>

<output>
Ultrathink on a detailed plan (docs/PLAN.md) on how to achieve our tasks to be discussed with me. The following points should be included in the plan:
- Prepare a github private repo in this root folder. Only allowed users should be able read, only myself can write. For each meaningful step in the plan we should have
a commit with a detailed massage.
- Once discussions with the plan are done, we shall create docs/ROADMAP.md with all information needed to evolve step by step on the documentation creation, 
proposals and system design artifacts and finally the prototype. Additionally, we shall have a JOURNAL.md, a companion of the ROADMAP.md which will also serve as an ADR, 
an architecture decisions records.
- The ultimate goal here is to have a prototype, minimum to make our main points and justify our position and approach of the product development.
- A written proposal or/and presentation with a system design view.
- A nice summary of how claude code was used to generate the repo. We might want to have a similar journal to highlight the prototyping process aceleration.
</output>

<uncertainty_policy>
- Never invent or estimate a number that isn't in the data you actually have.
- The source of truth are always the following documents in order: PLAN.md, ROADMAP.md and JOURNAL.md
- Register issues with the prefix ASSIST-XXX, where XXX is integers from 0-999, like ASSIST-001 ... ASSIST-999.
</uncertainty_policy>

Audience: CXOs. Tone: clear and professional. Be concise — lead with the highest-impact recommendation. No filler.